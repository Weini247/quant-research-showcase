"""Verify the exact public release file set and its SHA-256 checksums offline."""
from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parent
EXCLUDED={'PUBLIC_FILE_MANIFEST.json'}
def verify():
 manifest=json.loads((ROOT/'PUBLIC_FILE_MANIFEST.json').read_text(encoding='utf-8'))
 expected=manifest['files'];actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.relative_to(ROOT).parts and '.git' not in p.relative_to(ROOT).parts and p.relative_to(ROOT).as_posix() not in EXCLUDED}
 if actual!=set(expected):raise ValueError('PUBLIC_FILE_SET_MISMATCH')
 for name,record in expected.items():
  p=(ROOT/name).resolve()
  if not p.is_relative_to(ROOT.resolve()):raise ValueError('UNSAFE_MANIFEST_PATH')
  raw=p.read_bytes()
  if len(raw)!=record['bytes'] or hashlib.sha256(raw).hexdigest()!=record['sha256']:raise ValueError('PUBLIC_FILE_HASH_MISMATCH: '+name)
 return {'status':'PASS','files':len(expected),'manifest_excludes_itself':True,'scope':'file integrity only; no scientific validation'}
if __name__=='__main__':
 try:print(json.dumps(verify(),sort_keys=True))
 except (ValueError,OSError) as error:print(str(error),file=sys.stderr);sys.exit(1)
