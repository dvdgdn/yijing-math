"""Parser and provenance tests on synthetic source maps, without research findings."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('literature', Path(__file__).resolve().parents[1]/'literature.py')
lit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lit)

SAMPLE = '''# Collection
**001. Example family.** Neutral description. ([Lean](lean/docs/001.md))
<td>
&emsp;[Example <i>A</i>](preprints/example-a/paper.pdf)
An abstract about channels &amp; comparisons.
</td>
<td>
&emsp;[Example B](preprints/example-b/main.pdf)
A different abstract.
</td>
'''


class LiteratureTests(unittest.TestCase):
    def test_parse_preserves_all_papers_abstracts_and_scope(self):
        records = lit.parse_catalogue(SAMPLE)
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0]['title'], 'Example A')
        self.assertEqual(records[0]['abstract'], 'An abstract about channels & comparisons.')
        self.assertEqual(records[0]['family_formalization_scope'], 'lean/docs/001.md')
        self.assertEqual(SAMPLE.splitlines()[records[0]['source_line']-1], '&emsp;[Example <i>A</i>](preprints/example-a/paper.pdf)')

    def test_duplicate_links_are_not_independent_entries(self):
        with self.assertRaisesRegex(ValueError, 'duplicate manuscript'):
            lit.parse_catalogue(SAMPLE.replace('preprints/example-b/main.pdf', 'preprints/example-a/paper.pdf'))

    def test_empty_or_unlinked_maps_are_rejected(self):
        for text in ('No map.', '**001. Example.** No paper.'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                lit.parse_catalogue(text)

    def test_family_numbers_can_have_gaps(self):
        records = lit.parse_catalogue(SAMPLE+'**004. Other family.**\n&emsp;[Example C](preprints/example-c/paper.pdf)\nOther abstract.</td>')
        self.assertEqual({r['family'] for r in records}, {'001','004'})
        self.assertEqual(len(records),3)

    def test_tags_do_not_automatically_promote_review_or_priority(self):
        with tempfile.TemporaryDirectory() as directory:
            source=Path(directory)/'source.md';source.write_text(SAMPLE)
            config={'screening_rules':{'retrieval':['channel']},'reviewed_papers':{}}
            result=lit.build(source,config,'test-revision')
            self.assertEqual(result['records'][0]['screening_tags'],['retrieval'])
            self.assertEqual(result['records'][0]['review']['level'],'not individually reviewed')
            self.assertEqual(result['records'][0]['review']['priority'],'unassigned')
            self.assertEqual(result['source_sha256'],hashlib.sha256(source.read_bytes()).hexdigest())

    def test_check_detects_stale_catalogue_and_does_not_write(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);source=root/'source.md';config=root/'config.json';catalogue=root/'catalogue.json'
            source.write_text(SAMPLE);config.write_text('{}')
            result=lit.build(source,{},'test-revision')
            catalogue.write_text(json.dumps(result))
            command=['literature.py','check','--source',str(source),'--config',str(config),'--commit','test-revision','--catalogue',str(catalogue)]
            before=catalogue.read_bytes()
            with patch('sys.argv',command),contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(lit.main(),0)
            source.write_text(SAMPLE+'\nChanged input.\n')
            with patch('sys.argv',command),contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(lit.main(),1)
            self.assertEqual(catalogue.read_bytes(),before)

    def test_explicit_judgment_stays_distinct_from_keyword_tags(self):
        with tempfile.TemporaryDirectory() as directory:
            source=Path(directory)/'source.md';source.write_text(SAMPLE)
            config={'screening_rules':{},'reviewed_papers':{'preprints/example-a/paper.pdf':{'level':'statement inspected','priority':'conditional'}}}
            result=lit.build(source,config,'test-revision')
            self.assertEqual(result['records'][0]['review']['level'],'statement inspected')
            self.assertEqual(result['records'][0]['screening_tags'],[])
            self.assertEqual(result['records'][1]['review']['level'],'not individually reviewed')


if __name__=='__main__':
    unittest.main()
