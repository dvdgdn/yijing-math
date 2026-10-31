#!/usr/bin/env python3
"""Index a manuscript-map snapshot and search its titles and abstracts.

Source content, screening rules, and judgments are supplied as inputs, not embedded
in tooling. Screening tags retrieve candidates; they do not establish relevance,
correctness, novelty, or priority. Standard library only, Python 3.9+.
"""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re


FAMILY = re.compile(r'^\*\*(\d{3})\.\s+(.*?)\*\*', re.M)
PAPER = re.compile(r'&emsp;\[(.*?)\]\((preprints/[^\n]*?\.pdf)\)', re.S)


def plain(text):
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', text)).split())


def parse_catalogue(text):
    families = list(FAMILY.finditer(text))
    records = []
    paths = set()
    for i, family in enumerate(families):
        end = families[i+1].start() if i+1 < len(families) else len(text)
        block = text[family.end():end]
        papers = list(PAPER.finditer(block))
        if not papers:
            raise ValueError('family %s contains no paper links' % family[1])
        scope = re.search(r'\[Lean\]\((lean/docs/[^)]+)\)', block[:papers[0].start()])
        for paper in papers:
            path = paper[2]
            if path in paths:
                raise ValueError('duplicate manuscript path: '+path)
            paths.add(path)
            abstract = block[paper.end():].split('</td>', 1)[0]
            records.append(dict(family=family[1], family_title=plain(family[2]),
                                title=plain(paper[1]), path=path, abstract=plain(abstract),
                                source_line=text.count('\n', 0, family.end()+paper.start())+1,
                                family_formalization_scope=scope[1] if scope else None))
    if not records:
        raise ValueError('no manuscripts found')
    return records


def build(source, config, commit):
    data = source.read_bytes()
    records = parse_catalogue(data.decode('utf-8'))
    rules = config.get('screening_rules', {})
    review = config.get('reviewed_papers', {})
    base = 'https://github.com/openai/math/blob/'+commit+'/'
    for record in records:
        haystack = (record['family_title']+' '+record['title']+' '+record['abstract']).lower()
        record['screening_tags'] = [tag for tag, terms in rules.items() if any(re.search(term, haystack) for term in terms)]
        record['screening_level'] = 'automated title-and-abstract retrieval; not a proof review'
        record['review'] = review.get(record['path'], {'level': 'not individually reviewed', 'priority': 'unassigned'})
        record['url'] = base+record['path']
    return dict(commit=commit, source_sha256=hashlib.sha256(data).hexdigest(),
                manuscripts=len(records), families=len({r['family'] for r in records}),
                screening_warning='Tags retrieve candidates. No tag or catalogue entry is a verification or novelty claim.',
                records=records)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    p = commands.add_parser('build')
    p.add_argument('--source', type=Path, required=True)
    p.add_argument('--config', type=Path, required=True)
    p.add_argument('--commit', required=True)
    p.add_argument('--out', type=Path, required=True)
    p = commands.add_parser('check')
    p.add_argument('--source', type=Path, required=True)
    p.add_argument('--config', type=Path, required=True)
    p.add_argument('--commit', required=True)
    p.add_argument('--catalogue', type=Path, required=True)
    p = commands.add_parser('search')
    p.add_argument('--catalogue', type=Path, required=True)
    p.add_argument('terms', nargs='+')
    args = parser.parse_args()
    if args.command in {'build', 'check'}:
        result = build(args.source, json.loads(args.config.read_text()), args.commit)
        if args.command == 'check':
            if json.loads(args.catalogue.read_text()) != result:
                print('error: catalogue differs from source/configuration; rebuild it')
                return 1
            print('catalogue matches the pinned source and screening configuration')
        else:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
            print('%d manuscripts, %d families; indexed all titles and abstracts' % (result['manuscripts'], result['families']))
    else:
        data = json.loads(args.catalogue.read_text())
        terms = [t.lower() for t in args.terms]
        for r in data['records']:
            text = ' '.join([r['title'], r['abstract'], r['family_title']]+r['screening_tags']).lower()
            if all(term in text for term in terms):
                print('%s | %s | %s | %s' % (r['family'], r['title'], r['review']['level'], r['url']))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
