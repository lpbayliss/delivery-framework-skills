#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
import hashlib, sys
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'; errors=[]
skills=sorted(p.name for p in (ROOT/'skills').iterdir() if (p/'SKILL.md').is_file())
expected={f'{n}.skill' for n in skills}|{f'{n}.zip' for n in skills}|{'delivery-framework-skills.zip'}
actual={p.name for p in DIST.iterdir()} if DIST.is_dir() else set()
if actual!=expected: errors.append(f'archive set mismatch missing={sorted(expected-actual)} extra={sorted(actual-expected)}')
for n in skills:
    a=DIST/f'{n}.skill'; b=DIST/f'{n}.zip'
    if not a.is_file() or not b.is_file(): continue
    if hashlib.sha256(a.read_bytes()).digest()!=hashlib.sha256(b.read_bytes()).digest(): errors.append(f'{n}: .skill/.zip differ')
    with ZipFile(a) as z:
        if z.testzip(): errors.append(f'{n}: corrupt archive')
        names=z.namelist()
        if f'{n}/SKILL.md' not in names: errors.append(f'{n}: missing top-level SKILL.md')
        if any(not x.startswith(n+'/') for x in names): errors.append(f'{n}: out-of-prefix member')
        if any(any(bad in x.split('/') for bad in ['.git','dist','node_modules','__pycache__']) for x in names): errors.append(f'{n}: forbidden member')
plugin=DIST/'delivery-framework-skills.zip'
if plugin.is_file():
    with ZipFile(plugin) as z:
        if z.testzip(): errors.append('plugin: corrupt archive')
        names=set(z.namelist())
        for n in skills:
            if f'skills/{n}/SKILL.md' not in names: errors.append(f'plugin: missing {n}')
        for req in ['.claude-plugin/plugin.json','.claude-plugin/marketplace.json','README.md','LICENSE']:
            if req not in names: errors.append(f'plugin: missing {req}')
if errors:
    print('Package checks failed:',file=sys.stderr)
    for e in errors: print(f'- {e}',file=sys.stderr)
    raise SystemExit(1)
print(f'Package checks passed ({len(skills)} skills, {len(expected)} archives).')
