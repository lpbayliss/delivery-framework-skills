#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo
import shutil
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'; FIXED=(2020,1,1,0,0,0)
FORBIDDEN={'.git','dist','node_modules','__pycache__'}
def allowed(p): return not any(x in FORBIDDEN for x in p.parts) and not p.name.endswith(('.pyc','.env','.pem','.key'))
def add(z,src,arc):
    info=ZipInfo(arc,FIXED); info.compress_type=ZIP_DEFLATED; info.external_attr=(0o100644<<16)
    z.writestr(info,src.read_bytes(),compress_type=ZIP_DEFLATED,compresslevel=9)
def build(path,members):
    with ZipFile(path,'w') as z:
        for src,arc in sorted(members,key=lambda x:x[1]): add(z,src,arc)
if DIST.exists(): shutil.rmtree(DIST)
DIST.mkdir()
skills=sorted(p for p in (ROOT/'skills').iterdir() if (p/'SKILL.md').is_file())
for skill in skills:
    members=[(p,f'{skill.name}/{p.relative_to(skill).as_posix()}') for p in skill.rglob('*') if p.is_file() and allowed(p.relative_to(ROOT))]
    target=DIST/f'{skill.name}.skill'; build(target,members); shutil.copyfile(target,DIST/f'{skill.name}.zip')
plugin=[]
for p in ROOT.rglob('*'):
    rel=p.relative_to(ROOT)
    if not p.is_file() or not allowed(rel): continue
    if rel.parts[0] in {'.github','.claude-plugin','skills'} or rel.as_posix() in {'README.md','LICENSE','CONTRIBUTING.md'}:
        plugin.append((p,rel.as_posix()))
build(DIST/'delivery-framework-skills.zip',plugin)
print(f'Built {len(skills)*2+1} archives for {len(skills)} skills.')
