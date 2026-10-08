"""Test spec.claims_unrounded (việc treo nhà máy Tập 5): claims.json phải ghi giá trị CHƯA làm tròn của out/model.json raw.
Chạy: python3 toolkit/tests/test_claims_unrounded.py"""
import json, os, sys, tempfile, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'toolkit', 'factory'))
import spec as SPEC  # noqa: E402


def episode(d, value, raw=0.1234567, rounded=0.12):
    os.makedirs(os.path.join(d, 'out'), exist_ok=True)
    json.dump({'model': {'claims': {'c1': 'k1', 'c2': 'k2'}}}, open(os.path.join(d, 'contract.json'), 'w'))
    json.dump({'raw': {'k1': raw, 'k2': '2026-09-01'}, 'rounded': {'k1': rounded}}, open(os.path.join(d, 'out', 'model.json'), 'w'))
    json.dump({'claims': [{'claimId': 'c1', 'value': value}, {'claimId': 'c2', 'value': '2026-09-01'}]}, open(os.path.join(d, 'claims.json'), 'w'))
    return {'claims': 'claims.json'}


class T(unittest.TestCase):
    def test_raw_passes(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(SPEC.claims_unrounded(episode(d, 0.1234567), d), [])

    def test_rounded_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            P = SPEC.claims_unrounded(episode(d, 0.12), d)
            self.assertEqual([p['level'] for p in P], ['BLOCK'])
            self.assertIn('ROUNDED', P[0]['msg'])

    def test_no_contract_skips(self):
        with tempfile.TemporaryDirectory() as d:
            json.dump({'claims': [{'claimId': 'c1', 'value': 0.12}]}, open(os.path.join(d, 'claims.json'), 'w'))
            self.assertEqual(SPEC.claims_unrounded({'claims': 'claims.json'}, d), [])

    def test_ep005_clean(self):   # Tập 5 C5c: build_inputs.py đã ghi raw → 0 vi phạm
        ep = os.path.join(ROOT, 'episodes', 'ep005')
        self.assertEqual(SPEC.claims_unrounded({'claims': 'out/claims.json'}, ep), [])


if __name__ == '__main__':
    unittest.main()
