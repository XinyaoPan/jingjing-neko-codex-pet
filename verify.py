"""Read-only distribution integrity check, Python 3 standard library only."""
import hashlib,json,struct
from pathlib import Path
root=Path(__file__).resolve().parent
meta=json.loads((root/'pet.json').read_text(encoding='utf-8'))
png=(root/meta['spritesheet']).read_bytes()
assert png[:8]==b'\x89PNG\r\n\x1a\n','Not a PNG'
assert struct.unpack('>II',png[16:24])==(meta['width'],meta['height']),'Wrong dimensions'
assert hashlib.sha256(png).hexdigest()==meta['sha256'],'Spritesheet hash mismatch'
count=0
for line in (root/'checksums.sha256').read_text(encoding='utf-8').splitlines():
    digest,name=line.split('  ',1)
    path=(root/name).resolve()
    assert root==path or root in path.parents,'Unsafe manifest path'
    assert hashlib.sha256(path.read_bytes()).hexdigest()==digest,'Hash mismatch: '+name
    count+=1
print(f'OK: {count} files verified; v{meta["spriteVersionNumber"]}, {meta["width"]}x{meta["height"]}, {sum(meta["framesPerRow"])} frames.')
