"""Checks on published aggregates and their interpretation; no private modules required."""
from pathlib import Path
import collections,csv,json,math,unittest
ROOT=Path(__file__).resolve().parent
class AggregateTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.data=json.loads((ROOT/'aggregates.json').read_text(encoding='utf-8'))
 def test_scope_is_development_only(self):
  d=self.data;self.assertEqual(d['study']['development_years'],[2018,2019]);self.assertEqual(d['study']['origins'],98);self.assertEqual(d['study']['main_jobs'],490);self.assertFalse(d['study']['independent_validation']);self.assertEqual(len(d['study']['variants']),5)
 def test_point_comparisons_reconcile(self):
  d=self.data;zero={r['horizon']:r['scaled_mae'] for r in d['performance'] if r['variant']=='zero'}
  for p in d['paired']:
   if not p['contrast'].endswith('-minus-zero'):continue
   v=p['contrast'].removesuffix('-minus-zero');r=next(r for r in d['performance'] if r['variant']==v and r['horizon']==p['horizon']);self.assertAlmostEqual(p['mean'],r['scaled_mae']-zero[p['horizon']],places=10)
 def test_complete_quarter_landscape_and_weighted_means(self):
  d=self.data;cells=d['quarterly_landscape'];self.assertEqual(len(cells),512);self.assertEqual(len({(r['variant'],r['horizon'],r['asset'],r['quarter']) for r in cells}),512)
  self.assertEqual(min(r['n'] for r in cells),8)
  for p in d['paired']:
   if not p['contrast'].endswith('-minus-zero'):continue
   rows=[r for r in cells if r['variant']==p['contrast'].removesuffix('-minus-zero') and r['horizon']==p['horizon']];self.assertEqual(sum(r['n'] for r in rows),784);mean=math.fsum(r['mean']*r['n'] for r in rows)/784;self.assertAlmostEqual(mean,p['mean'],places=10)
 def test_intervals_are_stored_diagnostics(self):
  for p in self.data['paired']:
   self.assertEqual(p['n_origins'],98)
   for c in p['intervals'].values():self.assertLessEqual(c['low'],c['high']);self.assertEqual(c['resamples'],2000);self.assertEqual(c['valid_resamples'],2000)
 def test_probabilistic_denominators_and_order(self):
  for r in self.data['calibration']:
   self.assertEqual(r['valid_rows'],784);self.assertEqual(r['invalid_rows'],0);self.assertEqual(sorted(i['nominal_coverage'] for i in r['intervals']),[.4,.6,.8]);self.assertFalse(r['conditional_only'])
   ix=sorted(r['intervals'],key=lambda i:i['nominal_coverage']);self.assertEqual([i['scaled_width'] for i in ix],sorted(i['scaled_width'] for i in ix))
 def test_resource_values_are_measured_fields_only(self):
  for r in self.data['resources']:
   self.assertEqual(set(r),{'variant_id','wall_seconds','peak_rss_bytes','origin_count','status'});self.assertEqual(r['origin_count'],98);self.assertGreater(r['wall_seconds'],0);self.assertGreater(r['peak_rss_bytes'],0)
 def test_no_individual_or_private_fields(self):
  banned={'origin','target_date','target','point','prediction_id','measurement_id','seed','coefficients','alpha','checkpoint_sha256','code_commit','run_id'}
  def walk(x):
   if isinstance(x,dict):
    self.assertFalse(banned.intersection(x));[walk(v) for v in x.values()]
   elif isinstance(x,list):[walk(v) for v in x]
  walk(self.data)
 def test_csv_projections(self):
  expected={'point-performance.csv':10,'quarterly-landscape.csv':512,'resources.csv':5,'paired-intervals.csv':30,'probabilistic-quality.csv':18}
  for name,n in expected.items():
   with (ROOT/'tables'/name).open(encoding='utf-8',newline='') as f:self.assertEqual(len(list(csv.DictReader(f))),n)
 def test_renderer_is_public_and_has_no_research_execution(self):
  script=(ROOT/'render_figures.py').read_text(encoding='utf-8-sig');self.assertNotIn('import torch',script);self.assertNotIn('quantlab',script);self.assertNotIn('requests.',script);self.assertIn('aggregates.json',script)
 def test_six_english_figure_pairs(self):
  svgs=list((ROOT/'figures').glob('F*.svg'));self.assertEqual(len(svgs),6)
  for p in svgs:
   self.assertTrue(p.with_suffix('.png').exists());x=p.read_text(encoding='utf-8');self.assertIn('Quant Research Lab public aggregate renderer',x);self.assertNotRegex(x,r'[\u00c3\u00e2]');self.assertNotIn('xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="https',x)
if __name__=='__main__':unittest.main()
