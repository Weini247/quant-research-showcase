"""Release regression checks; no fitting, inference or statistical resampling."""
from pathlib import Path
import base64,json,unittest,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[2]
class ReleaseTests(unittest.TestCase):
 def test_horizon_roles_and_contrast_counts(self):
  d=json.loads((ROOT/'research/fx-development/aggregates.json').read_text(encoding='utf-8'))
  self.assertEqual(d['study']['primary_horizon'],1)
  comparisons=[r for r in d['paired'] if r['contrast'].endswith('-minus-zero')]
  self.assertEqual(len(comparisons),8)
  self.assertEqual([sum(r['horizon']==h for r in comparisons) for h in (1,20)],[4,4])
 def test_f2_is_self_contained_hybrid_svg(self):
  root=ET.fromstring((ROOT/'research/fx-development/figures/F2-failure-landscape.svg').read_bytes())
  images=list(root.iter('{http://www.w3.org/2000/svg}image'));self.assertEqual(len(images),9)
  for image in images:
   ref=image.get('{http://www.w3.org/1999/xlink}href') or image.get('href')
   self.assertTrue(ref.startswith('data:image/png;base64,'));raw=base64.b64decode(ref.split(',',1)[1],validate=False);self.assertEqual(raw[:8],b'\x89PNG\r\n\x1a\n')
  self.assertGreater(len(list(root.iter('{http://www.w3.org/2000/svg}text'))),100)
 def test_public_status_is_release_version(self):
  for name in ['index.html','fx-development.html','README.md']:
   text=(ROOT/name).read_text(encoding='utf-8-sig');self.assertIn('2.1',text);self.assertNotIn('READY_FOR_'+'OWNER_REVIEW',text)
  d=json.loads((ROOT/'research/fx-development/aggregates.json').read_text(encoding='utf-8'));self.assertEqual(d['publication_status'],'RELEASE_V2_1')
if __name__=='__main__':unittest.main()
