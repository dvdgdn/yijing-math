"""Coordination and context-boundary regressions with synthetic, neutral fixtures."""
import contextlib
import copy
import hashlib
import importlib.util
import io
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("yj", Path(__file__).resolve().parents[1] / "yj.py")
yj = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(yj)


def ident(prefix, number, width=4):
    return "%s-%0*d" % (prefix, width, number)


def record(meta, body="", path="fixture.md"):
    return path, meta, body


class CoordinationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.root_patch = patch.object(yj, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        for directory in ("prompts", "context/objects", "data", "ledger", "roadmap/assignments"):
            (self.root / directory).mkdir(parents=True, exist_ok=True)
        for name in ("role", "charter", "handoff"):
            (self.root / ("prompts/%s.md" % name)).write_text("Neutral %s.\n" % name)
        (self.root / "FROZEN.sha256").write_text("")

    def assignment(self, number=1, **changes):
        meta = {field: [] for field in yj.ASN_FIELDS}
        meta.update(id=ident("ASN", number), title="Example", status="ready", role="explorer",
                    context_mode="minimal", purpose="exploration", role_prompt="prompts/role.md",
                    charter="prompts/charter.md", handoff="prompts/handoff.md", recommended_model="unknown",
                    replication_of="none", created="2026-10-31", work_items=["example-output"])
        meta.update(changes)
        return meta

    def write_assignment(self, meta):
        lines = ["---"]
        for key, value in meta.items():
            lines.append("%s: %s" % (key, "[" + ", ".join(value) + "]" if isinstance(value, list) else value))
        lines += ["---", "## Rationale (coordinator only)", "Private selection notes.",
                  "<!-- BEGIN ASSIGNMENT -->", "Investigate the supplied objects.", "<!-- END ASSIGNMENT -->",
                  "<!-- BEGIN ASSIGNMENT PART 2 -->", "Continue the fixed task.", "<!-- END ASSIGNMENT PART 2 -->"]
        path = self.root / ("roadmap/assignments/%s-example.md" % meta["id"])
        path.write_text("\n".join(lines) + "\n")
        return path

    def assignments_report(self, *metas, invs=None):
        asns = {}
        for meta in metas:
            path = self.write_assignment(meta)
            _, body = yj.split_front_matter(path.read_text())
            asns[meta["id"]] = record(meta, body, str(path.relative_to(self.root)))
        report = yj.Report()
        yj.check_assignments(asns, {}, invs or {}, {}, report, [])
        return report

    def test_duplicate_work_requires_reciprocal_declaration_and_rationale(self):
        a, b = self.assignment(), self.assignment(2)
        report = self.assignments_report(a, b)
        self.assertTrue(any("undeclared overlap" in e for e in report.errors))
        a["intentional_overlap"] = [b["id"]]
        b["intentional_overlap"] = [a["id"]]
        report = self.assignments_report(a, b)
        self.assertTrue(any("explain overlap" in e for e in report.errors))
        for own, partner in ((a, b), (b, a)):
            path = self.write_assignment(own)
            path.write_text(path.read_text().replace("Private selection notes.", "Independent comparison with " + partner["id"]))
        report = yj.Report()
        asns = yj.load_records("roadmap/assignments", "*.md", report, r"ASN-\d{4}")
        yj.check_assignments(asns, {}, {}, {}, report, [])
        self.assertEqual(report.errors, [])

    def test_completed_or_withdrawn_work_is_not_concurrent_overlap(self):
        a, b = self.assignment(), self.assignment(2, status="completed")
        self.assertEqual(list(yj.overlaps({a["id"]: record(a), b["id"]: record(b)})), [])

    def test_claim_overlap_counts_even_with_different_work_keys(self):
        a, b = self.assignment(claims=[ident("C", 1)]), self.assignment(2, work_items=["other-output"], claims=[ident("C", 1)])
        pairs = list(yj.overlaps({a["id"]: record(a), b["id"]: record(b)}))
        self.assertEqual(pairs[0][2], [ident("C", 1)])
        self.assertFalse(pairs[0][3])

    def test_ready_requires_completed_prerequisite_but_draft_can_wait(self):
        a, b = self.assignment(prerequisites=[ident("ASN", 2)]), self.assignment(2, work_items=["other-output"])
        self.assertTrue(any("unfinished prerequisite" in e for e in self.assignments_report(a, b).errors))
        a["status"] = "draft"
        self.assertEqual(self.assignments_report(a, b).errors, [])
        a["status"], b["status"] = "ready", "completed"
        b["investigations"] = [ident("INV", 2)]
        invs = {ident("INV", 2): record(dict(status="registered", assignment=b["id"]))}
        self.assertEqual(self.assignments_report(a, b, invs=invs).errors, [])

    def test_completed_requires_registered_linked_output(self):
        meta = self.assignment(status="completed")
        self.assertTrue(any("requires a linked investigation" in e for e in self.assignments_report(meta).errors))
        iid = ident("INV", 1)
        meta["investigations"] = [iid]
        invs = {iid: record(dict(status="completed", assignment=meta["id"]))}
        self.assertTrue(any("unregistered investigation" in e for e in self.assignments_report(meta, invs=invs).errors))
        invs[iid][1]["status"] = "registered"
        self.assertEqual(self.assignments_report(meta, invs=invs).errors, [])
        invs[iid][1]["assignment"] = ident("ASN", 2)
        self.assertTrue(any("point back" in e for e in self.assignments_report(meta, invs=invs).errors))

    def test_malformed_material_list_reports_error(self):
        report = self.assignments_report(self.assignment(materials="prompts/charter.md"))
        self.assertTrue(any("materials must be a list" in e for e in report.errors))

    def test_unknown_target_is_rejected(self):
        meta = self.assignment(directions=[ident("DIR", 1, 3)])
        self.assertTrue(any("directions refers to unknown" in e for e in self.assignments_report(meta).errors))

    def test_dependency_diamond_and_cycle(self):
        ids = [ident("C", i) for i in range(1, 5)]
        claims = {ids[0]: record({"depends_on": []}), ids[1]: record({"depends_on": [ids[0]]}),
                  ids[2]: record({"depends_on": [ids[0]]}), ids[3]: record({"depends_on": ids[1:3]})}
        self.assertEqual(yj.downstream(claims, [ids[0]]), set(ids[1:]))
        report = yj.Report()
        yj.check_cycles(claims, "depends_on", report)
        self.assertEqual(report.errors, [])
        claims[ids[0]][1]["depends_on"] = [ids[3]]
        yj.check_cycles(claims, "depends_on", report)
        self.assertTrue(any("cycle" in e for e in report.errors))
        self.assertEqual(yj.downstream(claims, [ids[0]]), set(ids[1:]))

    def test_assignment_prerequisite_cycle_is_rejected(self):
        a = self.assignment(status="draft", prerequisites=[ident("ASN", 2)])
        b = self.assignment(2, status="draft", prerequisites=[a["id"]], work_items=["other-output"])
        self.assertTrue(any("prerequisites cycle" in e for e in self.assignments_report(a, b).errors))

    def test_package_excludes_all_coordinator_metadata(self):
        meta = self.assignment(directions=[ident("DIR", 1, 3)])
        self.write_assignment(meta)
        package = yj.build_package(meta["id"], 1)
        self.assertIn("Investigate the supplied objects.", package)
        for forbidden in ("Private selection notes", "directions:", "work_items:", ident("DIR", 1, 3)):
            self.assertNotIn(forbidden, package)

    def test_minimal_boundary_covers_all_components_and_later_phase(self):
        (self.root / "ledger/result.md").write_text("A result with no identifiers.\n")
        for field in ("role_prompt", "charter", "handoff", "materials", "materials_part2"):
            with self.subTest(field=field):
                value = ["ledger/result.md"] if field.startswith("materials") else "ledger/result.md"
                meta = self.assignment(**{field: value})
                self.write_assignment(meta)
                with self.assertRaisesRegex(ValueError, "minimal package"):
                    yj.build_package(meta["id"], 2 if field == "materials_part2" else 1)

    def test_canonical_paths_and_symlinks_cannot_bypass_context_boundary(self):
        secret = self.root / "ledger/result.md"
        secret.write_text("A result with no identifiers.\n")
        (self.root / "data/alias.md").symlink_to(secret)
        for path in ("data/../ledger/result.md", "data/alias.md"):
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, "minimal package"):
                yj.package_path(path, "minimal")
        with self.assertRaisesRegex(ValueError, "outside the repository"):
            yj.package_path(str(self.root.parent / "outside.md"), "full")
        self.assertEqual(yj.package_path("prompts/../prompts/role.md", "minimal"), self.root / "prompts/role.md")

    def test_targeted_rejects_board_and_summary_even_with_alternate_path(self):
        for path in ("roadmap/BOARD.md", "ledger/summary.md"):
            (self.root / path).write_text("Coordinator context.\n")
            with self.assertRaisesRegex(ValueError, "full-context"):
                yj.package_path("data/../" + path, "targeted")
            self.assertEqual(yj.package_path(path, "full"), self.root / path)

    def test_overwrite_never_replaces_frozen_file_including_alias(self):
        meta = self.assignment()
        self.write_assignment(meta)
        target = self.root / "original.md"
        original = b"Preserved original.\n"
        target.write_bytes(original)
        (self.root / "FROZEN.sha256").write_text(hashlib.sha256(original).hexdigest() + "  original.md\n")
        alias = self.root / "alias.md"
        alias.symlink_to(target)
        for output in (target, alias):
            args = Namespace(assignment=meta["id"], part=1, inv=None, out=str(output), overwrite=True)
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(yj.assemble(args), 1)
            self.assertEqual(target.read_bytes(), original)

    def test_board_distinguishes_source_work_and_unassigned_territory(self):
        direction = ident("DIR", 1, 3)
        (self.root / "ledger/directions.md").write_text("### %s — Example area\n" % direction)
        a = self.assignment(directions=[direction], purpose="source-work")
        asns = {a["id"]: record(a, path="roadmap/assignments/%s-example.md" % a["id"])}
        text = yj.render_plan({}, {}, asns, {direction: "ledger/directions.md"})
        self.assertIn("**unassigned** | " + a["id"] + " (ready; source-work)", text)

    def test_board_keeps_completed_unregistered_reports_visible(self):
        iid = ident("INV", 1)
        invs = {iid: record(dict(status="completed", title="Pending report", context_mode="full", independence="context-exposed"))}
        text = yj.render_plan({}, invs, {}, {})
        self.assertIn("Reports awaiting registration", text)
        self.assertIn(iid + ": Pending report", text)
        invs[iid][1]["status"] = "registered"
        text = yj.render_plan({}, invs, {}, {})
        self.assertNotIn(iid + ": Pending report", text)

    def test_impact_lists_transitive_dependents_and_does_not_mutate(self):
        a, b, c = [ident("C", i) for i in range(1, 4)]
        claims = {a: record({"depends_on": [], "status": "refuted", "title": "A"}),
                  b: record({"depends_on": [a], "status": "reported", "title": "B"}),
                  c: record({"depends_on": [b], "status": "reported", "title": "C"})}
        meta = self.assignment(claims=[c])
        records = claims, {}, {meta["id"]: record(meta)}, {}
        before = copy.deepcopy(records)
        output = io.StringIO()
        with patch.object(yj, "load_all", return_value=records), contextlib.redirect_stdout(output):
            self.assertEqual(yj.impact(Namespace(id=a)), 0)
        self.assertIn(c, output.getvalue())
        self.assertIn(meta["id"], output.getvalue())
        self.assertEqual(before, records)


class VerificationTests(unittest.TestCase):
    def check(self, source_family="family-a", verifier_family="family-b", **changes):
        cid, source, verifier = ident("C", 1), ident("INV", 1), ident("INV", 2)
        meta = {key: [] for key in yj.CLAIM_FIELDS}
        meta.update(id=cid, title="Example", type="theorem", status="verified", polarity="positive", domain="formal",
                    contingency="definitional", evidence="Example argument.", sources=[source], verifiers=[verifier],
                    value="unknown", registered="2026-10-31", updated="2026-10-31")
        vm = dict(model_family=verifier_family, role="verifier", status="completed", independence="isolated")
        vm.update(changes)
        invs = {source: record({"model_family": source_family}), verifier: record(vm)}
        body = "\n".join("## " + section + "\nExample.\n" for section in yj.CLAIM_SECTIONS)
        report = yj.Report()
        yj.check_claims({cid: record(meta, body)}, invs, {}, report)
        return report

    def test_completed_isolated_different_family_can_qualify(self):
        self.assertEqual(self.check().errors, [])

    def test_unknown_family_or_exposure_never_establishes_independence(self):
        cases = [dict(source_family="unknown"), dict(verifier_family="unknown"), dict(verifier_family="family-a"),
                 dict(status="running"), dict(independence="unknown"), dict(independence="context-exposed"), dict(role="explorer")]
        for case in cases:
            with self.subTest(case=case):
                self.assertTrue(any("status verified requires" in e for e in self.check(**case).errors))

    def test_verifier_cannot_also_be_an_originator(self):
        report = yj.Report()
        cid, iid = ident("C", 1), ident("INV", 1)
        meta = {key: [] for key in yj.CLAIM_FIELDS}
        meta.update(id=cid, title="Example", type="theorem", status="verified", polarity="positive", domain="formal",
                    contingency="definitional", evidence="Example argument.", sources=[iid], verifiers=[iid],
                    value="unknown", registered="2026-10-31", updated="2026-10-31")
        yj.check_claims({cid: record(meta)}, {iid: record(dict(model_family="family-a", role="verifier", status="completed", independence="isolated"))}, {}, report)
        self.assertTrue(any("status verified requires" in e for e in report.errors))


if __name__ == "__main__":
    unittest.main()
