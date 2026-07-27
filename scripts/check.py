#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SKILLS=ROOT/'skills'
errors=[]
def fail(x): errors.append(x)
def read(p):
    if not p.is_file(): fail(f'missing: {p.relative_to(ROOT)}'); return ''
    return p.read_text(encoding='utf-8')
def load(p):
    try: return json.loads(read(p))
    except json.JSONDecodeError as e: fail(f'invalid JSON {p.relative_to(ROOT)}: {e}'); return None
for rel in ['README.md','LICENSE','CONTRIBUTING.md','docs/framework-basis.md','docs/design-decisions.md','docs/framework-gaps.md','docs/notion-linear-model.md','docs/research-sources.md','docs/evaluation.md','.claude-plugin/plugin.json','.claude-plugin/marketplace.json','scripts/package_skill.py','scripts/check_packages.py']:
    read(ROOT/rel)
skill_dirs=sorted(p for p in SKILLS.iterdir() if (p/'SKILL.md').is_file()) if SKILLS.is_dir() else []
if len(skill_dirs)<2: fail('expected multiple skills')
for d in skill_dirs:
    text=read(d/'SKILL.md')
    m=re.match(r'^---\n(.*?)\n---\n',text,re.S)
    if not m: fail(f'{d.name}: invalid frontmatter'); continue
    fields={}
    for line in m.group(1).splitlines():
        if ':' in line: k,v=line.split(':',1); fields[k.strip()]=v.strip().strip('"')
    if fields.get('name')!=d.name: fail(f'{d.name}: frontmatter name mismatch')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',d.name): fail(f'{d.name}: invalid name')
    if not fields.get('description') or len(fields['description'])>1024: fail(f'{d.name}: invalid description')
    if len(text.splitlines())>500: fail(f'{d.name}: SKILL.md over 500 lines')
    for ref in set(re.findall(r'references/[A-Za-z0-9._-]+\.md',text)):
        if not (d/ref).is_file(): fail(f'{d.name}: missing {ref}')
    for template in set(re.findall(r'templates/[A-Za-z0-9._-]+\.md',text)):
        if not (d/template).is_file(): fail(f'{d.name}: missing {template}')
    ev=load(d/'evals/evals.json'); tr=load(d/'evals/trigger-evals.json')
    if not isinstance(ev,dict) or ev.get('skill_name')!=d.name: fail(f'{d.name}: invalid eval envelope')
    else:
        cases=ev.get('evals',[]); ids=[x.get('id') for x in cases if isinstance(x,dict)]
        if len(cases)<3 or len(ids)!=len(set(ids)): fail(f'{d.name}: need 3 unique evals')
        for x in cases:
            if not all(x.get(k) for k in ['id','kind','prompt','expected_output']): fail(f'{d.name}: incomplete eval')
            if len(x.get('assertions',[]))<4: fail(f'{d.name}: eval needs assertions')
    if not isinstance(tr,list) or len(tr)!=20: fail(f'{d.name}: need 20 trigger evals')
    elif sum(x.get('should_trigger') is True for x in tr)!=10 or sum(x.get('should_trigger') is False for x in tr)!=10: fail(f'{d.name}: trigger balance')
    common_contract=['Source precedence','workspace','Linear','Notion','Do not invent']
    for phrase in common_contract:
        if phrase not in text: fail(f'{d.name}: missing common contract phrase {phrase!r}')
semantic_contracts={
    'delivery-ticket-writing':['acceptance criteria','spike','risk'],
    'delivery-work-triage':['duplicate','return for refinement','relative placement'],
    'delivery-readiness-audit':['readiness ladder','leave alone','work-item age'],
    'delivery-ceremony-facilitation':['facilitator/MC','one or two experiments','Never fabricate'],
    'delivery-artifact-authoring':['traceability','postmortems','rollback'],
    'delivery-lifecycle-guidance':['gate','document exists','Move backward'],
    'delivery-backlog-reset':['real delivery system','Blocked work remains WIP','follow-up health checks'],
}
for name,phrases in semantic_contracts.items():
    corpus=read(SKILLS/name/'SKILL.md')+'\n'+''.join(read(p) for p in (SKILLS/name/'references').glob('*.md'))
    for phrase in phrases:
        if phrase not in corpus: fail(f'{name}: missing semantic contract phrase {phrase!r}')
public_corpus='\n'.join(read(p) for p in ROOT.rglob('*.md') if not any(x in p.parts for x in ['.git','dist']))
for forbidden in ['Application Insights','LaunchDarkly','Rootly','Databricks','Amplitude','Stan']:
    if forbidden in public_corpus: fail(f'organization-specific tool leaked into public content: {forbidden}')
for md in ROOT.rglob('*.md'):
    if any(x in md.parts for x in ['.git','dist']): continue
    text=read(md)
    for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',text):
        rel=target.split('#',1)[0]
        if not rel or '://' in rel or rel.startswith('mailto:'): continue
        if not (md.parent/rel).resolve().exists(): fail(f'broken link {md.relative_to(ROOT)} -> {target}')
for p in ROOT.rglob('*'):
    if p.is_file() and p.name.lower().endswith(('.env','.pem','.key')): fail(f'forbidden sensitive-looking file: {p.relative_to(ROOT)}')
if errors:
    print('Checks failed:',file=sys.stderr)
    for e in errors: print(f'- {e}',file=sys.stderr)
    raise SystemExit(1)
print(f'Repository checks passed ({len(skill_dirs)} skills).')
