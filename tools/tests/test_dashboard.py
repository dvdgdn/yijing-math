"""Dashboard provenance, family-fit and safe-rendering tests on neutral fixtures."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC=importlib.util.spec_from_file_location('dashboard',Path(__file__).resolve().parents[1]/'dashboard.py')
dash=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dash)


def ident(prefix,n,width=4):
    return '%s-%0*d'%(prefix,width,n)


def rec(meta,body='',path='fixture.md'):
    return path,meta,body


class DashboardTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for name in ['ledger','roadmap','investigations','context','tools']:
            (self.root/name).mkdir()
        self.cid,self.aid,self.iid=ident('C',1),ident('ASN',1),ident('INV',1)
        self.claim=dict(id=self.cid,title='Example statement',status='reported',sources=[self.iid],verifiers=[])
        self.assignment=dict(id=self.aid,title='Example assignment',status='ready',role='verifier',purpose='verification',
                             claims=[self.cid],prerequisites=[],investigations=[],replication_of='none',directions=[],questions=[])
        self.investigation=dict(id=self.iid,title='Example report',status='completed',model_family='gpt',context_mode='full',independence='context-exposed')
        self.records=({self.cid:rec(self.claim,path='ledger/statement.md')},
                      {self.iid:rec(self.investigation,path='investigations/report.md')},
                      {self.aid:rec(self.assignment,path='roadmap/assignment.md')},{})
        for path in ['ledger/statement.md','investigations/report.md','roadmap/assignment.md']:
            (self.root/path).write_text('Neutral source.\n')

    def snapshot(self):
        return dash.data_snapshot(self.root,self.records,'test-version',{self.cid:[]},[])

    def test_counts_come_from_evidence_not_assignment_suggestions(self):
        self.investigation['status']='missing-output'
        self.assignment['status']='ready'
        data=self.snapshot()
        self.assertEqual(data['summary']['running'],0)
        self.assertEqual(data['summary']['verified'],0)
        self.assertEqual(data['summary']['missing'],1)
        self.assertEqual(data['summary']['assignment_statuses'],{'ready':1})
        self.investigation['status']='running'
        self.claim['status']='verified'
        data=self.snapshot()
        self.assertEqual(data['summary']['running'],1)
        self.assertEqual(data['summary']['verified'],1)

    def test_completed_report_is_pending_registration(self):
        data=self.snapshot()
        self.assertEqual(data['summary']['pending_registration'],1)
        self.assertEqual(data['summary']['claims'],1)
        self.assertEqual(data['summary']['verified'],0)

    def test_same_family_and_unknown_provenance_cannot_be_independent_fit(self):
        claims,invs,_,_=self.records
        self.assertEqual(dash.family_fit(self.assignment,'gpt',claims,invs),'reproduction-only')
        self.assertEqual(dash.family_fit(self.assignment,'claude',claims,invs),'eligible')
        self.investigation['model_family']='unknown'
        self.assertEqual(dash.family_fit(self.assignment,'claude',claims,invs),'check-provenance')

    def test_replication_target_provenance_is_used_for_local_claims(self):
        claims,invs,_,_=self.records
        self.assignment['claims']=[]
        self.assignment['replication_of']=self.iid
        self.assertEqual(dash.family_fit(self.assignment,'claude',claims,invs),'eligible')
        self.assertEqual(dash.family_fit(self.assignment,'gpt',claims,invs),'reproduction-only')

    def test_explicit_model_exclusion_is_respected(self):
        claims,invs,_,_=self.records
        self.assignment['excluded_models']=['Claude']
        self.assertEqual(dash.family_fit(self.assignment,'claude',claims,invs),'excluded')
        self.assignment['role']='explorer'
        self.assertEqual(dash.family_fit(self.assignment,'claude',claims,invs),'excluded')

    def test_prerequisite_gates_are_derived_from_current_records(self):
        another=ident('ASN',2)
        self.assignment['prerequisites']=[another]
        data=self.snapshot()
        self.assertEqual(data['assignments'][0]['waiting_for'],[another])
        self.records[2][another]=rec(dict(id=another,status='completed',role='specialist',purpose='source-work',claims=[],prerequisites=[],investigations=[]),path='roadmap/other.md')
        data=self.snapshot()
        self.assertEqual(data['assignments'][0]['waiting_for'],[])

    def test_source_change_changes_fingerprint_without_changing_counts(self):
        before=self.snapshot()
        (self.root/'ledger/statement.md').write_text('A revised source record.\n')
        after=self.snapshot()
        self.assertNotEqual(before['fingerprint'],after['fingerprint'])
        self.assertEqual(before['summary'],after['summary'])

    def test_unknown_editorial_assignment_is_rejected(self):
        (self.root/'roadmap/dashboard-notes.json').write_text(json.dumps({'tracks':[{'assignments':[ident('ASN',99)]}]}))
        with self.assertRaisesRegex(ValueError,'unknown assignment'):
            self.snapshot()

    def test_malformed_editorial_shape_is_rejected(self):
        for notes in [None, [], {'tracks':None}, {'tracks':['incorrect']}]:
            with self.subTest(notes=notes):
                (self.root/'roadmap/dashboard-notes.json').write_text(json.dumps(notes))
                with self.assertRaises(ValueError):
                    self.snapshot()

    def test_script_end_tags_in_source_cannot_escape_data_container(self):
        data=self.snapshot()
        data['claims'][0]['title']='</script><img src=x onerror=alert(1)>'
        html=dash.render(data)
        blob=html.split('<script id="research-data" type="application/json">',1)[1].split('</script>',1)[0]
        self.assertNotIn('<img',blob)
        self.assertEqual(json.loads(blob)['claims'][0]['title'],data['claims'][0]['title'])
        self.assertIn('\\u003c/script',blob)

    def test_render_is_deterministic_and_has_no_external_asset_dependencies(self):
        data=self.snapshot()
        self.assertEqual(dash.render(data),dash.render(copy.deepcopy(data)))
        html=dash.render(data)
        self.assertNotIn('@@DATA@@',html)
        self.assertNotIn('<script src=',html)
        self.assertNotIn('fonts.googleapis.com',html)
        self.assertIn('<noscript>',html)

    def test_snapshot_does_not_mutate_the_records(self):
        before=copy.deepcopy(self.records)
        self.snapshot()
        self.assertEqual(self.records,before)

    def test_direction_intake_is_not_research_coverage(self):
        direction=ident('DIR',1,3)
        (self.root/'ledger/directions.md').write_text('### '+direction+' — Example territory\n\n*Status:* unexplored.\n')
        self.assignment['directions']=[direction]
        self.assignment['purpose']='source-work'
        self.assignment['role']='specialist'
        self.records[3][direction]='ledger/directions.md'
        row=self.snapshot()['directions'][0]
        self.assertEqual(row['research'],[])
        self.assertEqual(row['enabling'],[self.aid])


if __name__=='__main__':
    unittest.main()
