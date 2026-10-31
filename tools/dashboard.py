"""Read-only research dashboard built from repository records, with no embedded findings.

The HTML is a generated full-context artifact. UI sources stay in tools/dashboard;
editorial priorities, if present, are read from roadmap/dashboard-notes.json.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ASSETS = Path(__file__).with_name('dashboard')
INPUTS = ('ledger/CHANGELOG.md', 'roadmap/dashboard-notes.json',
          'roadmap/literature/openai-math/catalogue.json', 'methods/research-cycle.md',
          'methods/context-modes.md', 'methods/ledger-conventions.md', 'methods/standards.md',
          'investigations/_template/record.md')
ACTIVE = {'draft', 'ready', 'launched'}


def input_fingerprint(root, records):
    paths = {path for group in records[:3] for path, _, _ in group.values()}
    paths.update(records[3].values())
    paths.update(INPUTS)
    paths.update('tools/dashboard/' + p.name for p in ASSETS.iterdir() if p.is_file())
    paths.update(('tools/dashboard.py', 'tools/yj.py'))
    digest = hashlib.sha256()
    for name in sorted(paths):
        path = root / name
        digest.update(name.encode('utf-8') + b'\0')
        digest.update(path.read_bytes() if path.is_file() else b'<absent>')
        digest.update(b'\0')
    return digest.hexdigest()


def section_records(root, path, prefix):
    source = root / path
    if not source.exists():
        return []
    text = source.read_text(encoding='utf-8')
    matches = list(re.finditer(r'^### (' + re.escape(prefix) + r'-\d+) — (.+)$', text, re.M))
    rows = []
    for i, match in enumerate(matches):
        body = text[match.end():matches[i+1].start() if i+1 < len(matches) else len(text)]
        status = re.search(r'\*Status:\*\s*([^\n.]+)', body)
        rows.append(dict(id=match[1], title=match[2], status=status[1].strip() if status else 'unknown',
                         path=path, text=body.strip()))
    return rows


def family_fit(meta, family, claims, invs):
    excluded = any(str(name).lower() == family or str(name).lower().startswith(family + ' ')
                   for name in meta.get('excluded_models', []))
    if meta.get('role') != 'verifier':
        return 'excluded' if excluded else 'eligible'
    origins = set()
    for cid in meta.get('claims') or []:
        for iid in claims.get(cid, ('', {}, ''))[1].get('sources') or []:
            origins.add(invs.get(iid, ('', {}, ''))[1].get('model_family', 'unknown'))
    replication = meta.get('replication_of')
    if replication in invs:
        origins.add(invs[replication][1].get('model_family', 'unknown'))
    if family in origins:
        return 'reproduction-only'
    if excluded:
        return 'excluded'
    if not origins or 'unknown' in origins:
        return 'check-provenance'
    return 'eligible'


def data_snapshot(root, records, version, dependency_map, overlap_rows):
    claims, invs, asns, others = records
    notes_path = root / 'roadmap/dashboard-notes.json'
    notes = json.loads(notes_path.read_text()) if notes_path.exists() else {'tracks': []}
    if not isinstance(notes, dict) or not isinstance(notes.get('tracks', []), list):
        raise ValueError('dashboard notes must be an object with a tracks list')
    for track in notes.get('tracks', []):
        if not isinstance(track, dict) or not isinstance(track.get('assignments', []), list):
            raise ValueError('each dashboard priority must be an object with an assignments list')
        for aid in track.get('assignments', []):
            if not isinstance(aid, str) or aid not in asns:
                raise ValueError('dashboard priority refers to an unknown assignment: ' + str(aid))
    assignments = []
    for aid, (path, meta, _) in sorted(asns.items()):
        row = dict(meta, path=path)
        row['waiting_for'] = [ref for ref in meta.get('prerequisites', [])
                              if ref not in asns or asns[ref][1].get('status') != 'completed']
        row['claude_fit'] = family_fit(meta, 'claude', claims, invs)
        row['gpt_fit'] = family_fit(meta, 'gpt', claims, invs)
        row['runs'] = [iid for iid in meta.get('investigations', []) if iid in invs]
        assignments.append(row)
    claim_rows = []
    for cid, (path, meta, _) in sorted(claims.items()):
        row = dict(meta, path=path, dependents=sorted(dependency_map.get(cid, [])))
        row['verification_work'] = [a['id'] for a in assignments if a['role'] == 'verifier'
                                    and a['status'] in ACTIVE and cid in a.get('claims', [])]
        claim_rows.append(row)
    investigation_rows = [dict(meta, path=path) for _, (path, meta, _) in sorted(invs.items())]
    directions = section_records(root, 'ledger/directions.md', 'DIR')
    questions = section_records(root, 'ledger/questions.md', 'Q')
    disputes = section_records(root, 'ledger/disputes.md', 'DSP')
    for direction in directions:
        matches = [a for a in assignments if direction['id'] in a.get('directions', [])]
        direction['research'] = [a['id'] for a in matches if a['status'] in ACTIVE and a['purpose'] not in {'source-work','prior-art'}]
        direction['enabling'] = [a['id'] for a in matches if a['status'] in ACTIVE and a['purpose'] in {'source-work','prior-art'}]
        direction['completed'] = [a['id'] for a in matches if a['status'] == 'completed']
    for question in questions:
        question['assignments'] = [a['id'] for a in assignments if question['id'] in a.get('questions', []) and a['status'] in ACTIVE]
    corpus_path = root / 'roadmap/literature/openai-math/catalogue.json'
    corpus = json.loads(corpus_path.read_text()) if corpus_path.exists() else {}
    papers = [dict(title=p['title'], family=p['family'], family_title=p['family_title'], url=p['url'],
                   tags=p.get('screening_tags', []), review=p.get('review', {})) for p in corpus.get('records', [])]
    claim_counts = dict(Counter(c['status'] for c in claim_rows))
    assignment_counts = dict(Counter(a['status'] for a in assignments))
    inv_counts = dict(Counter(i['status'] for i in investigation_rows))
    known_dates = [m.get(key, '') for group in records[:3] for _, m, _ in group.values()
                   for key in ('updated', 'registered', 'created', 'date_run')
                   if re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(m.get(key, '')))]
    return dict(schema=1, fingerprint=input_fingerprint(root, records), version=version,
                record_date=max(known_dates) if known_dates else None,
                summary=dict(claims=len(claim_rows), claim_statuses=claim_counts,
                             assignments=len(assignments), assignment_statuses=assignment_counts,
                             investigations=len(investigation_rows), investigation_statuses=inv_counts,
                             running=inv_counts.get('running', 0),
                             pending_registration=inv_counts.get('completed', 0),
                             missing=inv_counts.get('missing-output', 0),
                             verified=claim_counts.get('verified', 0)),
                assignments=assignments, claims=claim_rows, investigations=investigation_rows,
                directions=directions, questions=questions, disputes=disputes,
                overlaps=[dict(a=a, b=b, shared=shared, declared=declared) for a,b,shared,declared in overlap_rows],
                corpus=dict(papers=papers, families=len({p['family'] for p in papers}),
                            inspected=sum(p['review'].get('level', '').startswith('theorem') for p in papers),
                            commit=corpus.get('commit')), notes=notes)


def safe_json(data):
    text = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    for original, escaped in [('<', '\\u003c'), ('>', '\\u003e'), ('&', '\\u0026'), ('\u2028', '\\u2028'), ('\u2029', '\\u2029')]:
        text = text.replace(original, escaped)
    return text


def render(data):
    template = (ASSETS / 'template.html').read_text(encoding='utf-8')
    for token, value in [('@@STYLE@@', (ASSETS / 'style.css').read_text(encoding='utf-8')),
                         ('@@DATA@@', safe_json(data)),
                         ('@@SCRIPT@@', (ASSETS / 'app.js').read_text(encoding='utf-8'))]:
        if template.count(token) != 1:
            raise ValueError('dashboard template must contain exactly one ' + token)
        template = template.replace(token, value)
    return template


def write(root, data):
    path = root / 'roadmap/dashboard.html'
    content = render(data)
    if not path.exists() or path.read_text(encoding='utf-8') != content:
        # A same-directory replacement prevents browsers seeing partially written HTML.
        temporary = path.with_suffix('.html.tmp')
        temporary.write_text(content, encoding='utf-8')
        temporary.replace(path)
    return path


def serve(root, refresh, port):
    """Serve local documents and refresh from valid records; never accept mutations."""
    root = root.resolve()
    allowed_roots = {'roadmap','ledger','investigations','context','methods','prompts','data','compute','tools'}
    allowed_suffixes = {'.html','.md','.json','.csv','.txt','.py','.tex','.yaml','.yml'}

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(root), **kwargs)

        def log_message(self, *_args):
            pass

        def do_GET(self):
            request = unquote(urlsplit(self.path).path)
            if request == '/__dashboard_status':
                payload = refresh()
                payload['checked_at'] = datetime.now(timezone.utc).isoformat()
                body = json.dumps(payload).encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Cache-Control', 'no-store')
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            if request == '/':
                self.send_response(302)
                self.send_header('Location','/roadmap/dashboard.html')
                self.end_headers()
                return
            relative = Path(request.lstrip('/'))
            candidate = (root / relative).resolve()
            try:
                resolved = candidate.relative_to(root)
            except ValueError:
                self.send_error(403)
                return
            if (any(part.startswith('.') for part in relative.parts) or
                (resolved.parts and resolved.parts[0] not in allowed_roots and len(resolved.parts) > 1) or
                candidate.suffix not in allowed_suffixes or not candidate.is_file()):
                self.send_error(404)
                return
            if request == '/roadmap/dashboard.html':
                refresh()
            self.path = '/' + resolved.as_posix()
            super().do_GET()

        def do_HEAD(self):
            self.send_error(405, 'Use GET for this read-only preview')

        def end_headers(self):
            self.send_header('Cache-Control','no-cache')
            self.send_header('X-Content-Type-Options','nosniff')
            super().end_headers()

        def list_directory(self, _path):
            self.send_error(404)
            return None

    server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    print('Local: http://127.0.0.1:%d/roadmap/dashboard.html' % server.server_port, flush=True)
    print('Reads repository records automatically; only valid changes update the snapshot. Ctrl+C to stop.', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
