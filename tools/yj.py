#!/usr/bin/env python3
"""Lightweight tooling for the yijing-math research repository.

Standard library only (Python 3.9+). Run from anywhere:

    python3 tools/yj.py validate            # check the repository; exit 1 on errors
    python3 tools/yj.py index               # regenerate ledger/INDEX.md
    python3 tools/yj.py assemble ASN-0001 [--part 2] [--inv INV-0003] [--out FILE]

The conventions this enforces are documented in methods/ledger-conventions.md,
methods/context-modes.md and prompts/README.md.
"""
import argparse
import hashlib
import re
import sys
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
    "id", "title", "status", "role", "assignment", "model", "model_identifier", "prompt",
    "prompt_version", "context_mode", "materials", "output", "handoff", "date_run",
    "registered", "preceded_by", "followed_by",
]
ASN_STATUSES = {"draft", "ready", "launched", "completed", "withdrawn"}
ASN_FIELDS = [
    "id", "title", "status", "role", "context_mode", "role_prompt", "charter", "handoff",
    "materials", "materials_part2", "claims", "recommended_model", "excluded_models",
    "replication_of", "investigations", "created",
]
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


def model_family(name):
    match = re.match(r"\s*([A-Za-z]+)", name or "")
    return match.group(1).lower() if match else ""


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
            if not (v.startswith("human:") or v in invs):
                report.error(where, "verifier %s is neither human:<name> nor a known investigation" % v)
        status = meta.get("status")
        if status in ("reproduced", "verified") and not verifiers:
            report.error(where, "status %s requires at least one verifier" % status)
        if status == "verified":
            origin = {model_family(invs[s][1].get("model")) for s in sources if s in invs}
            independent = [v for v in verifiers if v.startswith("human:") or
                           (v in invs and model_family(invs[v][1].get("model")) not in origin)]
            if not independent:
                report.error(where, "status verified requires a human verifier or one from a "
                                    "different model family than every source; use 'reproduced'")
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
        assignment = meta.get("assignment", "none")
        if assignment not in ("none", "unknown") and assignment not in asns:
            report.error(where, "assignment %s not found" % assignment)
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


def check_assignments(asns, claims, invs, report, leak_terms):
    for aid, (where, meta, body) in asns.items():
        for field in ASN_FIELDS:
            if field not in meta:
                report.error(where, "missing field %r" % field)
        if meta.get("status") not in ASN_STATUSES:
            report.error(where, "status %r not in vocabulary" % meta.get("status"))
        if meta.get("role") not in ROLES - {"legacy"}:
            report.error(where, "role %r not in vocabulary" % meta.get("role"))
        mode = meta.get("context_mode")
        if mode not in MODES:
            report.error(where, "context_mode %r not in vocabulary" % mode)
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


def clean_files():
    for entry in CLEAN_PATHS:
        path = ROOT / entry
        if path.is_file():
            yield path
        elif path.is_dir():
            for f in sorted(path.rglob("*")):
                if f.is_file() and f.suffix in (".md", ".txt", ".csv", ".py") and "__pycache__" not in f.parts:
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


def validate(_args):
    report = Report()
    frozen = check_frozen(report)
    claims, invs, asns, others = load_all(report)
    leak_terms = load_leak_terms()
    check_claims(claims, invs, others, report)
    check_investigations(invs, asns, frozen, report)
    check_assignments(asns, claims, invs, report, leak_terms)
    check_clean_files(report, leak_terms)
    check_references(claims, invs, asns, others, frozen, report)
    index_path = ROOT / "ledger/INDEX.md"
    if not index_path.exists() or index_path.read_text(encoding="utf-8") != render_index(claims):
        report.warn("ledger/INDEX.md", "out of date; run: python3 tools/yj.py index")
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
    report = Report()
    claims = load_records("ledger/claims", "C-*.md", report, r"C-\d{4}")
    if report.errors:
        print("\n".join("error: " + e for e in report.errors))
        return 1
    (ROOT / "ledger/INDEX.md").write_text(render_index(claims), encoding="utf-8")
    print("wrote ledger/INDEX.md (%d claims)" % len(claims))
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
    sub.add_parser("index", help="regenerate ledger/INDEX.md").set_defaults(func=index)
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
