#!/usr/bin/env python3
"""Lightweight tooling for the yijing-math research repository.

Standard library only (Python 3.9+). Run from anywhere:

    python3 tools/yj.py validate            # check the repository; exit 1 on errors
    python3 tools/yj.py index               # regenerate indexes and HTML dashboard
    python3 tools/yj.py plan                # coordinator board (full-context output)
    python3 tools/yj.py impact ID           # downstream claims and assignments
    python3 tools/yj.py assemble ASN-0001 [--part 2] [--inv INV-0003] [--out FILE]

The conventions this enforces are documented in methods/ledger-conventions.md,
methods/context-modes.md and prompts/README.md.
"""
import argparse
import hashlib
import importlib.util
import re
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CLAIM_TYPES = {
    "theorem", "construction", "computational-observation", "statistical-result",
    "conjecture", "hypothesis", "counterexample", "impossibility", "bounded-search",
    "inconclusive", "historical-claim", "interpretation",
}
NEGATIVE_TYPES = {"counterexample", "impossibility", "bounded-search", "inconclusive"}
STATUSES = {
    "reported", "in-verification", "reproduced", "verified", "disputed",
    "refuted", "superseded", "withdrawn",
}
POLARITIES = {"positive", "negative", "inconclusive"}
DOMAINS = {"formal", "source-dependent", "historical", "interpretive"}
CONTINGENCIES = {"definitional", "contingent", "mixed", "n/a"}
VALUES = {"high", "medium", "low", "unknown"}
CLAIM_FIELDS = [
    "id", "title", "type", "status", "polarity", "domain", "contingency", "evidence",
    "sources", "verifiers", "depends_on", "related", "competes_with", "supersedes",
    "superseded_by", "value", "registered", "updated",
]
CLAIM_SECTIONS = [
    "Statement", "Definitions and assumptions", "Provenance", "Evidence and verification",
    "Scope and limitations", "Objections and alternatives", "Further investigation",
]

ROLES = {"explorer", "specialist", "verifier", "synthesis", "paradigm-breaker", "coordinator", "legacy"}
MODES = {"minimal", "targeted", "full"}
INV_STATUSES = {"prepared", "running", "completed", "registered", "missing-output", "abandoned"}
INV_FIELDS = [
    "id", "title", "status", "role", "assignment", "model", "model_family", "independence", "model_identifier", "prompt",
    "prompt_version", "context_mode", "materials", "output", "handoff", "date_run",
    "registered", "preceded_by", "followed_by",
]
ASN_STATUSES = {"draft", "ready", "launched", "completed", "withdrawn"}
ASN_FIELDS = [
    "id", "title", "status", "role", "context_mode", "role_prompt", "charter", "handoff",
    "materials", "materials_part2", "claims", "recommended_model", "excluded_models",
    "replication_of", "investigations", "created",
    "directions", "questions", "work_items", "prerequisites", "intentional_overlap",
    "purpose",
]
ACTIVE_ASN = {"draft", "ready", "launched"}
PURPOSES = {"verification", "development", "exploration", "source-work", "prior-art", "synthesis", "reset"}
ENABLING = {"source-work", "prior-art"}
NOT_A_PATH = {"unknown", "missing", "none", ""}

LEDGER_ID_RE = re.compile(r"\b(?:C-\d{4}|DEF-\d{3}|Q-\d{3}|DIR-\d{3}|DSP-\d{3})\b")
OTHER_ID_RE = re.compile(r"\b(?:INV-\d{4}|ASN-\d{4}|SRC-\d{3})\b")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Files that may reach minimal-context investigators or be auto-loaded by agent tools.
CLEAN_PATHS = [
    "README.md", "AGENTS.md", "CLAUDE.md", "methods", "prompts", "context/objects",
    "data", "compute/README.md", "tools",
]
# Material a minimal-context package may include.
MINIMAL_ALLOWED = ("prompts/", "context/objects/", "data/", "methods/")
# Material that is full-context only and must not go into targeted packages either.
FULL_ONLY = ("ledger/summary.md", "ledger/INDEX.md", "ledger/leak-terms.txt")


class Report:
    def __init__(self):
        self.errors, self.warnings = [], []

    def error(self, where, msg):
        self.errors.append("%s: %s" % (where, msg))

    def warn(self, where, msg):
        self.warnings.append("%s: %s" % (where, msg))


def rel(path):
    return str(Path(path).resolve().relative_to(ROOT))


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def sha256_file(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def split_front_matter(text):
    """Return (meta, body). Front matter is a flat 'key: value' block between --- lines."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated front matter")
    meta = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError("front matter line without ':': %r" % line)
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            meta[key.strip()] = [v.strip() for v in inner.split(",") if v.strip()] if inner else []
        else:
            meta[key.strip()] = value
    return meta, text[end + 5:]


def strip_front_matter(text):
    return split_front_matter(text)[1]


def extract_block(body, name):
    begin, end = "<!-- BEGIN %s -->" % name, "<!-- END %s -->" % name
    if begin not in body or end not in body:
        return None
    inner = body.split(begin, 1)[1].split(end, 1)[0]
    if inner.startswith("\n"):
        inner = inner[1:]
    if inner.endswith("\n"):
        inner = inner[:-1]
    return inner


def heading_ids(path, prefix):
    pattern = re.compile(r"^### (%s-\d+) — " % prefix, re.M)
    return pattern.findall(read(path)) if (ROOT / path).exists() else []


def load_leak_terms():
    path = ROOT / "ledger/leak-terms.txt"
    if not path.exists():
        return []
    terms = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            terms.append(line)
    return terms


def find_leak_terms(text, terms):
    found = []
    for term in terms:
        pattern = re.escape(term)
        if term[:1].isalnum():
            pattern = r"(?<![A-Za-z0-9])" + pattern
        if term[-1:].isalnum():
            pattern = pattern + r"(?![A-Za-z0-9])"
        if re.search(pattern, text, re.I):
            found.append(term)
    return found


def model_family(meta):
    """Use recorded family, never infer independence from a model's display name."""
    family = str(meta.get("model_family", "unknown")).strip().lower()
    return "" if family in ("", "unknown", "none", "missing") else family


def named_human(ref):
    return isinstance(ref, str) and ref.startswith("human:") and bool(ref[6:].strip())


def package_path(path, mode):
    """Resolve every input before applying context boundaries (including symlinks)."""
    if not isinstance(path, str):
        raise ValueError("package paths must be strings")
    resolved = (ROOT / path).resolve()
    try:
        canonical = resolved.relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        raise ValueError("package input is outside the repository: %s" % path)
    if not resolved.is_file():
        raise ValueError("package input is not a file: %s" % path)
    if mode == "minimal" and not canonical.startswith(MINIMAL_ALLOWED):
        raise ValueError("minimal package may not include %s" % canonical)
    if mode != "full" and (canonical in FULL_ONLY or canonical.startswith("roadmap/")):
        raise ValueError("%s is coordinator/full-context material" % canonical)
    return resolved


def package_inputs(meta, part):
    if part == 1:
        return [meta[k] for k in ("role_prompt", "charter", "handoff")] + (meta.get("materials") or [])
    return meta.get("materials_part2") or []


def overlaps(asns):
    active = [(aid, rec[1]) for aid, rec in sorted(asns.items()) if rec[1].get("status") in ACTIVE_ASN]
    for i, (aid, a) in enumerate(active):
        for bid, b in active[i + 1:]:
            shared = set(a.get("work_items") or []) & set(b.get("work_items") or [])
            shared |= set(a.get("claims") or []) & set(b.get("claims") or [])
            if shared:
                declared = bid in (a.get("intentional_overlap") or []) and aid in (b.get("intentional_overlap") or [])
                yield aid, bid, sorted(shared), declared


def downstream(claims, roots):
    """Return transitive claim dependents; terminate even on invalid cyclic data."""
    seen, pending = set(roots), list(roots)
    while pending:
        current = pending.pop()
        for cid, (_, meta, _) in claims.items():
            if cid not in seen and current in (meta.get("depends_on") or []):
                seen.add(cid)
                pending.append(cid)
    return seen - set(roots)


# ---------------------------------------------------------------- loading

def load_records(directory, pattern, report, id_re):
    """Load front-matter records; returns {id: (path, meta, body)}."""
    records = {}
    for path in sorted((ROOT / directory).glob(pattern)):
        if "_template" in path.parts:
            continue
        where = rel(path)
        try:
            meta, body = split_front_matter(path.read_text(encoding="utf-8"))
        except ValueError as exc:
            report.error(where, str(exc))
            continue
        if meta is None or "id" not in meta:
            report.error(where, "missing front matter or id")
            continue
        rid = meta["id"]
        if not re.fullmatch(id_re, rid):
            report.error(where, "malformed id %r" % rid)
        stem = path.parent.name if path.name == "record.md" else path.stem
        if not (stem == rid or stem.startswith(rid + "-")):
            report.error(where, "id %s does not match file or folder name" % rid)
        if rid in records:
            report.error(where, "duplicate id %s" % rid)
        records[rid] = (where, meta, body)
    return records


def load_all(report):
    claims = load_records("ledger/claims", "C-*.md", report, r"C-\d{4}")
    invs = load_records("investigations", "INV-*/record.md", report, r"INV-\d{4}")
    asns = load_records("roadmap/assignments", "ASN-*.md", report, r"ASN-\d{4}")
    others = {}
    for path, prefix in [("ledger/definitions.md", "DEF"), ("ledger/questions.md", "Q"),
                         ("ledger/directions.md", "DIR"), ("ledger/disputes.md", "DSP"),
                         ("data/sources.md", "SRC")]:
        ids = heading_ids(path, prefix)
        for dup in sorted({i for i in ids if ids.count(i) > 1}):
            report.error(path, "duplicate id %s" % dup)
        for i in ids:
            others[i] = path
    return claims, invs, asns, others


# ---------------------------------------------------------------- checks

def check_frozen(report):
    manifest = ROOT / "FROZEN.sha256"
    frozen = set()
    if not manifest.exists():
        report.error("FROZEN.sha256", "missing")
        return frozen
    for n, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        if len(parts) != 2:
            report.error("FROZEN.sha256:%d" % n, "malformed line")
            continue
        digest, path = parts[0], parts[1].strip().lstrip("*")
        frozen.add(path)
        if not (ROOT / path).exists():
            report.error(path, "frozen file is missing")
        elif sha256_file(path) != digest:
            report.error(path, "frozen file has changed (SHA-256 mismatch)")
    return frozen


def check_claims(claims, invs, others, report):
    known = set(claims) | set(others)
    for cid, (where, meta, body) in claims.items():
        for field in CLAIM_FIELDS:
            if field not in meta:
                report.error(where, "missing field %r" % field)
        for field, vocab in [("type", CLAIM_TYPES), ("status", STATUSES), ("polarity", POLARITIES),
                             ("domain", DOMAINS), ("contingency", CONTINGENCIES), ("value", VALUES)]:
            if field in meta and meta[field] not in vocab:
                report.error(where, "%s %r not in vocabulary" % (field, meta[field]))
        for field in ("registered", "updated"):
            if field in meta and not DATE_RE.match(str(meta[field])):
                report.error(where, "%s must be YYYY-MM-DD" % field)
        list_fields = ["sources", "verifiers", "depends_on", "related", "competes_with",
                       "supersedes", "superseded_by"]
        for field in list_fields:
            if field in meta and not isinstance(meta[field], list):
                report.error(where, "%s must be a list" % field)
        sources = meta.get("sources") or []
        if not sources:
            report.error(where, "a claim needs at least one source investigation")
        for s in sources:
            if s not in invs:
                report.error(where, "source %s is not a known investigation" % s)
        for field in ["depends_on", "related", "competes_with", "supersedes", "superseded_by"]:
            for ref in meta.get(field) or []:
                if ref not in known:
                    report.error(where, "%s refers to unknown id %s" % (field, ref))
        verifiers = meta.get("verifiers") or []
        for v in verifiers:
            if not (named_human(v) or v in invs):
                report.error(where, "verifier %s is neither human:<name> nor a known investigation" % v)
        status = meta.get("status")
        if status in ("reproduced", "verified") and not verifiers:
            report.error(where, "status %s requires at least one verifier" % status)
        if status == "verified":
            origin = {model_family(invs[s][1]) for s in sources if s in invs}
            independent = [v for v in verifiers if named_human(v) or
                           (v in invs and v not in sources and origin and "" not in origin and
                            model_family(invs[v][1]) and model_family(invs[v][1]) not in origin and
                            invs[v][1].get("role") == "verifier" and
                            invs[v][1].get("status") in ("completed", "registered") and
                            invs[v][1].get("independence") == "isolated")]
            if not independent:
                report.error(where, "status verified requires a named human or a completed isolated verifier "
                                    "with known family distinct from every source and not also an originator")
        if status == "superseded" and not meta.get("superseded_by"):
            report.error(where, "status superseded requires superseded_by")
        if status == "refuted" and not (meta.get("related") or meta.get("superseded_by")):
            report.warn(where, "refuted claim should link its counterexample in related")
        # body sections, in order
        headings = re.findall(r"^## (.+?)\s*$", body, re.M)
        positions = []
        for section in CLAIM_SECTIONS:
            if section not in headings:
                report.error(where, "missing section '## %s'" % section)
            else:
                positions.append(headings.index(section))
        if positions != sorted(positions):
            report.error(where, "sections are out of order")
        negative = meta.get("polarity") in ("negative", "inconclusive") or meta.get("type") in NEGATIVE_TYPES
        if negative:
            scope = body.split("## Scope and limitations", 1)[-1].split("\n## ", 1)[0]
            if "Not ruled out:" not in scope:
                report.error(where, "negative or inconclusive claim needs a 'Not ruled out:' line in its scope")


def check_path_field(where, meta, field, report, must_exist):
    value = meta.get(field, "")
    if isinstance(value, list) or value in NOT_A_PATH:
        return None
    if must_exist and not (ROOT / value).exists():
        report.error(where, "%s path does not exist: %s" % (field, value))
    return value


def check_investigations(invs, asns, frozen, report):
    for iid, (where, meta, body) in invs.items():
        for field in INV_FIELDS:
            if field not in meta:
                report.error(where, "missing field %r" % field)
        if meta.get("status") not in INV_STATUSES:
            report.error(where, "status %r not in vocabulary" % meta.get("status"))
        if meta.get("role") not in ROLES:
            report.error(where, "role %r not in vocabulary" % meta.get("role"))
        if meta.get("context_mode") not in MODES | {"unknown"}:
            report.error(where, "context_mode %r not in vocabulary" % meta.get("context_mode"))
        if meta.get("independence") not in {"unknown", "isolated", "context-exposed"}:
            report.error(where, "independence must be unknown, isolated, or context-exposed")
        family = meta.get("model_family")
        if not isinstance(family, str) or not re.fullmatch(r"[a-z][a-z0-9-]*", family):
            report.error(where, "model_family must be an explicit lowercase family key or unknown")
        assignment = meta.get("assignment", "none")
        if assignment not in ("none", "unknown") and assignment not in asns:
            report.error(where, "assignment %s not found" % assignment)
        elif assignment in asns and iid not in (asns[assignment][1].get("investigations") or []):
            report.error(where, "investigation must be listed on its assignment %s" % assignment)
        status = meta.get("status")
        if status == "missing-output" and meta.get("output") != "missing":
            report.error(where, "status missing-output requires output: missing")
        sent = status in ("running", "completed", "registered")
        prompt = check_path_field(where, meta, "prompt", report, must_exist=True)
        output = check_path_field(where, meta, "output", report, must_exist=status in ("completed", "registered"))
        if status in ("completed", "registered") and output is None:
            report.error(where, "status %s requires an output path" % status)
        for path in (prompt, output):
            if sent and path and (ROOT / path).exists() and path not in frozen:
                report.warn(where, "%s is not listed in FROZEN.sha256" % path)


def check_assignments(asns, claims, invs, others, report, leak_terms):
    for aid, (where, meta, body) in asns.items():
        for field in ASN_FIELDS:
            if field not in meta:
                report.error(where, "missing field %r" % field)
        if meta.get("status") not in ASN_STATUSES:
            report.error(where, "status %r not in vocabulary" % meta.get("status"))
        if meta.get("role") not in ROLES - {"legacy"}:
            report.error(where, "role %r not in vocabulary" % meta.get("role"))
        if meta.get("purpose") not in PURPOSES:
            report.error(where, "purpose %r not in vocabulary" % meta.get("purpose"))
        mode = meta.get("context_mode")
        if mode not in MODES:
            report.error(where, "context_mode %r not in vocabulary" % mode)
        malformed_lists = False
        for field in ("materials", "materials_part2", "claims", "excluded_models", "investigations",
                      "directions", "questions", "work_items", "prerequisites", "intentional_overlap"):
            if not isinstance(meta.get(field), list):
                report.error(where, "%s must be a list" % field)
                malformed_lists = True
        if malformed_lists:
            continue
        for field, prefix in (("directions", "DIR-"), ("questions", "Q-")):
            for ref in meta.get(field) or []:
                if ref not in others or not ref.startswith(prefix):
                    report.error(where, "%s refers to unknown %s" % (field, ref))
        if not meta.get("work_items"):
            report.error(where, "work_items must name at least one concrete output")
        for key in meta.get("work_items") or []:
            if not re.fullmatch(r"[a-z][a-z0-9-]*", key):
                report.error(where, "work item must be a lowercase hyphenated key: %s" % key)
        rationale = body.split("## Rationale (coordinator only)", 1)[-1].split("\n## ", 1)[0]
        for field in ("prerequisites", "intentional_overlap"):
            for ref in meta.get(field) or []:
                if ref not in asns or ref == aid:
                    report.error(where, "%s must refer to another known assignment: %s" % (field, ref))
                elif field == "intentional_overlap" and ref not in rationale:
                    report.error(where, "explain overlap with %s in the coordinator rationale" % ref)
                elif field == "prerequisites" and meta.get("status") == "ready" and asns[ref][1].get("status") != "completed":
                    report.error(where, "ready assignment has unfinished prerequisite %s; keep it draft" % ref)
        replication = meta.get("replication_of", "none")
        if replication == aid or (replication not in {"none", "unknown"} and replication not in invs and replication not in asns):
            report.error(where, "replication_of refers to unknown assignment or investigation")
        for part in (1, 2):
            try:
                for path in package_inputs(meta, part):
                    package_path(path, mode)
            except (OSError, ValueError, KeyError) as exc:
                report.error(where, str(exc))
        for field in ("role_prompt", "charter", "handoff"):
            check_path_field(where, meta, field, report, must_exist=True)
        for field in ("materials", "materials_part2"):
            for path in meta.get(field) or []:
                if not (ROOT / path).exists():
                    report.error(where, "%s entry does not exist: %s" % (field, path))
                if path in FULL_ONLY and mode != "full":
                    report.error(where, "%s is full-context material" % path)
                if mode == "minimal" and not path.startswith(MINIMAL_ALLOWED):
                    report.error(where, "minimal assignment includes non-minimal material %s" % path)
        for cid in meta.get("claims") or []:
            if cid not in claims:
                report.error(where, "claim %s not found" % cid)
        for iid in meta.get("investigations") or []:
            if iid not in invs:
                report.error(where, "investigation %s not found" % iid)
            elif invs[iid][1].get("assignment") != aid:
                report.error(where, "investigation %s must point back to this assignment" % iid)
        run_ids = meta.get("investigations") or []
        if meta.get("status") in {"launched", "completed"} and not run_ids:
            report.error(where, "launched/completed assignment requires a linked investigation")
        if meta.get("status") == "completed":
            if any(iid in invs and invs[iid][1].get("status") not in {"registered", "abandoned"} for iid in run_ids):
                report.error(where, "completed assignment has unregistered investigation output")
            if not any(iid in invs and invs[iid][1].get("status") == "registered" for iid in run_ids):
                report.error(where, "completed assignment requires at least one registered investigation")
        if "## Rationale (coordinator only)" not in body:
            report.error(where, "missing '## Rationale (coordinator only)' section")
        text = extract_block(body, "ASSIGNMENT")
        if text is None:
            report.error(where, "missing BEGIN/END ASSIGNMENT markers")
            continue
        expected = meta.get("assignment_text_sha256")
        if expected and hashlib.sha256(text.encode("utf-8")).hexdigest() != expected:
            report.error(where, "assignment text no longer matches assignment_text_sha256")
        if meta.get("materials_part2") and extract_block(body, "ASSIGNMENT PART 2") is None:
            report.error(where, "materials_part2 given but no ASSIGNMENT PART 2 block")
        if mode == "minimal":
            try:
                package = build_package(aid, 1)
            except (OSError, ValueError) as exc:
                report.error(where, "cannot assemble: %s" % exc)
                continue
            ids = sorted(set(LEDGER_ID_RE.findall(package)))
            if ids:
                report.error(where, "minimal package mentions ledger ids: %s" % ", ".join(ids))
            terms = find_leak_terms(package, leak_terms)
            if terms:
                report.warn(where, "minimal package contains leak terms: %s" % ", ".join(terms))
    for aid, bid, shared, declared in overlaps(asns):
        if not declared:
            report.error(aid, "undeclared overlap with %s (%s); narrow scope or record intentional_overlap on both assignments" %
                         (bid, ", ".join(shared)))
    check_cycles(asns, "prerequisites", report)


def check_cycles(records, field, report):
    visited, active = set(), []

    def visit(rid):
        if rid in active:
            report.error(rid, "%s cycle: %s" % (field, " -> ".join(active[active.index(rid):] + [rid])))
            return
        if rid in visited:
            return
        visited.add(rid)
        active.append(rid)
        for ref in records[rid][1].get(field) or []:
            if ref in records:
                visit(ref)
        active.pop()

    for rid in records:
        visit(rid)


def clean_files():
    for entry in CLEAN_PATHS:
        path = ROOT / entry
        if path.is_file():
            yield path
        elif path.is_dir():
            for f in sorted(path.rglob("*")):
                if f.is_file() and f.suffix in (".md", ".txt", ".csv", ".py", ".html", ".css", ".js") and "__pycache__" not in f.parts:
                    yield f


def check_clean_files(report, leak_terms):
    for path in clean_files():
        text = path.read_text(encoding="utf-8")
        ids = sorted(set(LEDGER_ID_RE.findall(text)))
        if ids:
            report.error(rel(path), "clean file mentions ledger ids: %s" % ", ".join(ids))
        terms = find_leak_terms(text, leak_terms)
        if terms:
            report.error(rel(path), "clean file contains leak terms: %s" % ", ".join(terms))


def check_references(claims, invs, asns, others, frozen, report):
    known = set(claims) | set(invs) | set(asns) | set(others)
    # Worked examples may name the next unused investigation number.
    known.add("INV-%04d" % (max([int(i[4:]) for i in invs] or [0]) + 1))
    for path in sorted(ROOT.rglob("*.md")):
        relpath = rel(path)
        if relpath.startswith((".git/", ".claude/")) or relpath in frozen:
            continue
        text = path.read_text(encoding="utf-8")
        for ref in sorted(set(LEDGER_ID_RE.findall(text)) | set(OTHER_ID_RE.findall(text))):
            if ref not in known:
                report.error(relpath, "refers to unknown id %s" % ref)


def inspect_repository():
    report = Report()
    frozen = check_frozen(report)
    claims, invs, asns, others = load_all(report)
    leak_terms = load_leak_terms()
    check_claims(claims, invs, others, report)
    check_cycles(claims, "depends_on", report)
    check_investigations(invs, asns, frozen, report)
    check_assignments(asns, claims, invs, others, report, leak_terms)
    check_clean_files(report, leak_terms)
    check_references(claims, invs, asns, others, frozen, report)
    return (claims, invs, asns, others), frozen, report


def validate(_args):
    records, frozen, report = inspect_repository()
    claims, invs, asns, others = records
    index_path = ROOT / "ledger/INDEX.md"
    if not index_path.exists() or index_path.read_text(encoding="utf-8") != render_index(claims):
        report.warn("ledger/INDEX.md", "out of date; run: python3 tools/yj.py index")
    board_path = ROOT / "roadmap/BOARD.md"
    if not board_path.exists() or board_path.read_text(encoding="utf-8") != render_plan(claims, invs, asns, others):
        report.warn("roadmap/BOARD.md", "out of date; run: python3 tools/yj.py index")
    try:
        expected = dashboard_module().render(dashboard_snapshot(records))
        dashboard_path = ROOT / "roadmap/dashboard.html"
        if not dashboard_path.exists() or dashboard_path.read_text(encoding="utf-8") != expected:
            report.warn("roadmap/dashboard.html", "out of date; run: python3 tools/yj.py index")
    except (OSError, ValueError, KeyError) as exc:
        report.error("roadmap/dashboard.html", str(exc))
    for w in report.warnings:
        print("warning: " + w)
    for e in report.errors:
        print("error:   " + e)
    print("%d claims, %d investigations, %d assignments, %d other ids, %d frozen files: "
          "%d errors, %d warnings" % (len(claims), len(invs), len(asns), len(others), len(frozen),
                                      len(report.errors), len(report.warnings)))
    return 1 if report.errors else 0


# ---------------------------------------------------------------- index

INDEX_GROUPS = [
    ("Theorems and constructions", lambda m: m["type"] in ("theorem", "construction")),
    ("Computational observations", lambda m: m["type"] == "computational-observation"),
    ("Statistical results", lambda m: m["type"] == "statistical-result"),
    ("Conjectures and hypotheses", lambda m: m["type"] in ("conjecture", "hypothesis")),
    ("Historical claims and interpretations", lambda m: m["type"] in ("historical-claim", "interpretation")),
]


def ledger_version():
    path = ROOT / "ledger/CHANGELOG.md"
    match = re.search(r"^## (v[\d.]+)", path.read_text(encoding="utf-8"), re.M) if path.exists() else None
    return match.group(1) if match else "unknown"


def render_index(claims):
    rows = [meta for _, meta, _ in claims.values()]
    lines = [
        "# Claim Index",
        "",
        "Generated by `python3 tools/yj.py index` from `ledger/claims/`. Do not edit by hand.",
        "Ledger version: %s. **Full-context material.**" % ledger_version(),
        "",
        "Status counts: " + ", ".join(
            "%s %d" % (s, sum(1 for m in rows if m.get("status") == s))
            for s in sorted(STATUSES) if any(m.get("status") == s for m in rows)) + ".",
        "",
    ]
    negative = [m for m in rows if m.get("polarity") != "positive" or m.get("type") in NEGATIVE_TYPES]
    groups = [("Negative and inconclusive results", negative)]
    remaining = [m for m in rows if m not in negative]
    for title, test in INDEX_GROUPS:
        groups.append((title, [m for m in remaining if test(m)]))
    for title, members in groups:
        if not members:
            continue
        lines += ["## " + title, "",
                  "| ID | Title | Type | Status | Domain | Contingency | Value | Sources |",
                  "|---|---|---|---|---|---|---|---|"]
        for m in sorted(members, key=lambda m: m["id"]):
            lines.append("| [%s](claims/%s.md) | %s | %s | %s | %s | %s | %s | %s |" % (
                m["id"], m["id"], m.get("title", "").replace("|", "\\|"), m.get("type"),
                m.get("status"), m.get("domain"), m.get("contingency"), m.get("value"),
                ", ".join(m.get("sources") or [])))
        lines.append("")
    return "\n".join(lines)


def index(_args):
    records, frozen, report = inspect_repository()
    if report.errors:
        print("\n".join("error: " + e for e in report.errors))
        return 1
    write_exports(records, frozen)
    print("wrote ledger/INDEX.md (%d claims), roadmap/BOARD.md and roadmap/dashboard.html" % len(records[0]))
    return 0


_dashboard = None


def dashboard_module():
    global _dashboard
    if _dashboard is None:
        spec = importlib.util.spec_from_file_location("yj_dashboard", Path(__file__).with_name("dashboard.py"))
        _dashboard = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_dashboard)
    return _dashboard


def dashboard_snapshot(records):
    claims, invs, asns, others = records
    return dashboard_module().data_snapshot(ROOT, records, ledger_version(),
               {cid: downstream(claims, [cid]) for cid in claims}, list(overlaps(asns)))


def write_exports(records, frozen):
    claims, invs, asns, others = records
    targets = ("ledger/INDEX.md", "roadmap/BOARD.md", "roadmap/dashboard.html")
    if set(targets) & frozen:
        raise ValueError("refusing to regenerate a frozen export")
    data = dashboard_snapshot(records)
    # Render all exports before touching any existing export.
    index_text, board_text = render_index(claims), render_plan(*records)
    dashboard_module().render(data)
    (ROOT / targets[0]).write_text(index_text, encoding="utf-8")
    (ROOT / targets[1]).write_text(board_text, encoding="utf-8")
    dashboard_module().write(ROOT, data)
    return data


def dashboard(args):
    if index(args):
        return 1
    if not args.serve:
        return 0
    records, frozen, report = inspect_repository()
    last = {"valid": True, "fingerprint": dashboard_snapshot(records)["fingerprint"], "errors": []}
    lock = threading.Lock()

    def refresh():
        with lock:
            try:
                current, frozen, report = inspect_repository()
                if report.errors:
                    return dict(last, valid=False, errors=report.errors)
                data = dashboard_snapshot(current)
                if data["fingerprint"] != last["fingerprint"]:
                    write_exports(current, frozen)
                    last.update(fingerprint=data["fingerprint"])
                return dict(last)
            except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
                return dict(last, valid=False, errors=[str(exc)])

    dashboard_module().serve(ROOT, refresh, args.port)
    return 0


# ---------------------------------------------------------------- coordination (full-context output)

def render_plan(claims, invs, asns, others):
    lines = ["# Coordination Board", "", "**Full-context, coordinator-only material.** Never supply to isolated investigators.", "",
             "Generated by `python3 tools/yj.py index`; preview with `python3 tools/yj.py plan`.",
             "Assignment metadata records planned coverage; it is not evidence that a territory was investigated.", "",
             "## Work queue", "", "| Assignment | Status | Purpose / role / context | Waiting for | Work items |",
             "|---|---|---|---|---|"]
    for aid, (path, meta, _) in sorted(asns.items()):
        waiting = [ref for ref in meta.get("prerequisites") or []
                   if ref not in asns or asns[ref][1].get("status") != "completed"]
        lines.append("| [%s](%s) | %s | %s / %s / %s | %s | %s |" % (
            aid, Path(path).relative_to("roadmap").as_posix(), meta.get("status"), meta.get("purpose"), meta.get("role"),
            meta.get("context_mode"), ", ".join(waiting) or "—", ", ".join(meta.get("work_items") or [])))
    for title, prefix, field in (("Direction coverage", "DIR-", "directions"), ("Question coverage", "Q-", "questions")):
        lines += ["", "## " + title, "", "| Target | Active research assignments | Enabling assignments | Completed assignments |", "|---|---|---|---|"]
        for rid, path in sorted(others.items()):
            if not rid.startswith(prefix):
                continue
            active, enabling, completed = [], [], []
            for aid, (_, meta, _) in sorted(asns.items()):
                if rid in (meta.get(field) or []):
                    if meta.get("status") in ACTIVE_ASN:
                        bucket = enabling if meta.get("purpose") in ENABLING else active
                        bucket.append("%s (%s; %s)" % (aid, meta["status"], meta.get("purpose")))
                    elif meta.get("status") == "completed":
                        completed.append("%s (%s)" % (aid, meta.get("purpose")))
            lines.append("| [%s](../%s#%s) | %s | %s | %s |" % (
                rid, path, heading_anchor(path, rid), ", ".join(active) or "**unassigned**", ", ".join(enabling) or "—", ", ".join(completed) or "—"))
    lines += ["", "## Overlap review", "",
              "Exact shared work keys or claim targets are shown below. Read rationales before launch.",
              "Different wording can hide duplication; also compare assignments sharing a direction.", ""]
    pairs = list(overlaps(asns))
    if pairs:
        for aid, bid, shared, declared in pairs:
            lines.append("- %s / %s: %s — %s." % (
                aid, bid, ", ".join(shared), "declared intentional" if declared else "**UNDECLARED**"))
    else:
        lines.append("No shared work keys or claim targets among active assignments.")
    lines += ["", "## Verification debt", "",
              "Dependent counts are transitive claim counts, not importance scores. Verification owners are planned work, not verdicts.", "",
              "| Claim | Status | Value | Dependents | Active verifier assignments |", "|---|---|---|---|---|"]
    debt = [(cid, meta) for cid, (_, meta, _) in claims.items()
            if meta.get("status") in {"reported", "reproduced", "in-verification", "disputed"}]
    for cid, meta in sorted(debt, key=lambda item: (-len(downstream(claims, [item[0]])), item[0])):
        owners = [aid for aid, (_, ameta, _) in sorted(asns.items())
                  if ameta.get("role") == "verifier" and ameta.get("status") in ACTIVE_ASN and cid in (ameta.get("claims") or [])]
        lines.append("| [%s](../ledger/claims/%s.md) | %s | %s | %d | %s |" % (
            cid, cid, meta.get("status"), meta.get("value"), len(downstream(claims, [cid])), ", ".join(owners) or "—"))
    lines += ["", "## Dependencies needing review", "",
              "These are review triggers. A changed premise does not automatically refute a dependent claim.", ""]
    triggers = [(cid, meta) for cid, (_, meta, _) in sorted(claims.items())
                if meta.get("status") in {"refuted", "superseded", "withdrawn", "disputed"} and downstream(claims, [cid])]
    for cid, meta in triggers:
        lines.append("- %s (%s): review %s; run `python3 tools/yj.py impact %s`." % (
            cid, meta["status"], ", ".join(sorted(downstream(claims, [cid]))), cid))
    if not triggers:
        lines.append("No terminal or disputed premises with recorded claim dependents.")
    lines += ["", "## Missing research record", ""]
    missing = [iid for iid, (_, meta, _) in sorted(invs.items()) if meta.get("status") == "missing-output"]
    lines.append(", ".join(missing) + ": coverage and independence remain unknown until the output is recovered." if missing else "None recorded.")
    lines += ["", "## Reports awaiting registration", ""]
    pending = [(iid, meta) for iid, (_, meta, _) in sorted(invs.items()) if meta.get("status") == "completed"]
    for iid, meta in pending:
        lines.append("- %s: %s; context %s; independence %s. Review the output and registration draft before counting new claims." % (
            iid, meta.get("title"), meta.get("context_mode"), meta.get("independence")))
    if not pending:
        lines.append("None recorded.")
    lines += ["", "Selection decisions and semantic overlap: [coordination review](coordination-review.md). External-literature priorities, when present, are linked from the [roadmap](README.md).", ""]
    return "\n".join(lines)


def heading_anchor(path, rid):
    heading = next((line[4:] for line in read(path).splitlines() if line.startswith("### " + rid + " — ")), rid)
    return re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")


def plan(_args):
    report = Report()
    records = load_all(report)
    if report.errors:
        raise ValueError("; ".join(report.errors))
    print(render_plan(*records), end="")
    return 0


def impact(args):
    report = Report()
    claims, invs, asns, others = load_all(report)
    if report.errors:
        raise ValueError("; ".join(report.errors))
    if args.id not in set(claims) | set(others):
        raise ValueError("unknown claim, definition, question, direction, or source: %s" % args.id)
    affected = downstream(claims, [args.id])
    targets = affected | {args.id}
    print("Full-context dependency review for %s (no statuses changed)." % args.id)
    for cid in sorted(affected):
        meta = claims[cid][1]
        print("  %s [%s]: %s" % (cid, meta.get("status"), meta.get("title")))
    if not affected:
        print("  No recorded claim dependents. Check unrecorded data/source dependencies manually.")
    print("Assignments referring to the target or its claim dependents:")
    for aid, (_, meta, _) in sorted(asns.items()):
        refs = set(meta.get("claims") or []) | set(meta.get("directions") or []) | set(meta.get("questions") or [])
        material_text = " ".join((meta.get("materials") or []) + (meta.get("materials_part2") or []))
        refs |= set(LEDGER_ID_RE.findall(material_text)) | set(OTHER_ID_RE.findall(material_text))
        if refs & targets:
            print("  %s [%s]: %s" % (aid, meta.get("status"), ", ".join(sorted(refs & targets))))
    return 0


# ---------------------------------------------------------------- assemble

def find_assignment(aid):
    matches = sorted((ROOT / "roadmap/assignments").glob(aid + "-*.md")) + \
        sorted((ROOT / "roadmap/assignments").glob(aid + ".md"))
    if len(matches) != 1:
        raise ValueError("expected exactly one assignment file for %s, found %d" % (aid, len(matches)))
    return matches[0]


def build_package(aid, part, inv=None):
    meta, body = split_front_matter(find_assignment(aid).read_text(encoding="utf-8"))
    mode = meta.get("context_mode")
    if mode not in MODES:
        raise ValueError("unknown context_mode")
    for path in package_inputs(meta, part):
        package_path(path, mode)
    pieces = []
    if inv:
        pieces.append("Investigation ID: %s. Assignment: %s." % (inv, aid))
    if part == 1:
        text = extract_block(body, "ASSIGNMENT")
        if text is None:
            raise ValueError("%s has no ASSIGNMENT block" % aid)
        pieces.append(strip_front_matter(read(meta["role_prompt"])))
        pieces.append(strip_front_matter(read(meta["charter"])))
        for path in meta.get("materials") or []:
            pieces.append("## Supplied material: `%s`\n\n%s" % (path, strip_front_matter(read(path))))
        pieces.append(text)
        pieces.append(strip_front_matter(read(meta["handoff"])))
    else:
        text = extract_block(body, "ASSIGNMENT PART 2")
        if text is None:
            raise ValueError("%s has no ASSIGNMENT PART 2 block" % aid)
        pieces.append(text)
        for path in meta.get("materials_part2") or []:
            pieces.append("## Supplied material: `%s`\n\n%s" % (path, strip_front_matter(read(path))))
    return "\n\n---\n\n".join(p.strip("\n") for p in pieces) + "\n"


def assemble(args):
    meta, _ = split_front_matter(find_assignment(args.assignment).read_text(encoding="utf-8"))
    mode = meta.get("context_mode")
    materials = (meta.get("materials") if args.part == 1 else meta.get("materials_part2")) or []
    problems = []
    for path in materials:
        if path in FULL_ONLY and mode != "full":
            problems.append("%s is full-context material" % path)
        if mode == "minimal" and not path.startswith(MINIMAL_ALLOWED):
            problems.append("minimal package may not include %s" % path)
    package = build_package(args.assignment, args.part, args.inv)
    if mode == "minimal":
        ids = sorted(set(LEDGER_ID_RE.findall(package)))
        if ids:
            problems.append("minimal package mentions ledger ids: %s" % ", ".join(ids))
        terms = find_leak_terms(package, load_leak_terms())
        if terms:
            print("warning: minimal package contains leak terms: %s" % ", ".join(terms), file=sys.stderr)
    if problems:
        for p in problems:
            print("error: " + p, file=sys.stderr)
        return 1
    digest = hashlib.sha256(package.encode("utf-8")).hexdigest()
    if args.out:
        out = Path(args.out)
        if out.exists() and not args.overwrite:
            print("error: %s exists (prompts are frozen once sent; use --overwrite only if it was never sent)"
                  % out, file=sys.stderr)
            return 1
        frozen_report = Report()
        frozen = check_frozen(frozen_report)
        if any(out.resolve() == (ROOT / path).resolve() for path in frozen):
            print("error: refusing to overwrite a frozen file", file=sys.stderr)
            return 1
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(package, encoding="utf-8")
        print("wrote %s" % out, file=sys.stderr)
    else:
        sys.stdout.write(package)
    print("%s part %d (%s context), SHA-256 %s" % (args.assignment, args.part, mode, digest), file=sys.stderr)
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="check the repository").set_defaults(func=validate)
    sub.add_parser("index", help="regenerate claim index, coordination board and HTML dashboard").set_defaults(func=index)
    p = sub.add_parser("dashboard", help="rebuild the dashboard, optionally serving a live local view")
    p.add_argument("--serve", action="store_true", help="watch valid record changes through a local read-only server")
    p.add_argument("--port", type=int, default=8765, help="local server port (default: 8765)")
    p.set_defaults(func=dashboard)
    sub.add_parser("plan", help="show the full-context coordination board").set_defaults(func=plan)
    p = sub.add_parser("impact", help="review downstream claim dependencies (full context)")
    p.add_argument("id", help="a registered claim or other ledger/source id")
    p.set_defaults(func=impact)
    p = sub.add_parser("assemble", help="build the package to send to an investigator")
    p.add_argument("assignment", help="assignment id, e.g. ASN-0001")
    p.add_argument("--part", type=int, choices=(1, 2), default=1)
    p.add_argument("--inv", help="investigation id to state at the top of the package")
    p.add_argument("--out", help="write to this file instead of stdout")
    p.add_argument("--overwrite", action="store_true", help="overwrite --out if it exists")
    p.set_defaults(func=assemble)
    args = parser.parse_args()
    try:
        return args.func(args)
    except (OSError, ValueError, KeyError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
