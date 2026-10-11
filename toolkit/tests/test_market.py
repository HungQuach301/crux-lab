# Phiên Thị trường: các hàm không gọi mạng của toolkit/market (purge > 30 ngày, nhận chương, nhãn, đọc chương mô tả).
import datetime as dt, os, pathlib, sys, tempfile, unittest

HERE = pathlib.Path(__file__).resolve().parents[1] / 'market'
sys.path.insert(0, str(HERE))


class TestMarket(unittest.TestCase):
    def test_purge_older_than_30_days(self):
        with tempfile.TemporaryDirectory() as d:
            os.environ['MARKET_CACHE'] = d
            for n in ('2026-09-01', '2026-09-20', '2026-10-11', 'notes'):
                (pathlib.Path(d) / n).mkdir()
            import importlib, mcommon, purge
            importlib.reload(mcommon); importlib.reload(purge)
            gone = purge.purge(today=dt.date(2026, 10, 11))
            self.assertEqual([p.name for p in gone], ['2026-09-01'])
            self.assertTrue((pathlib.Path(d) / '2026-09-20').exists())
            del os.environ['MARKET_CACHE']

    def test_chapters_and_labels(self):
        from pull import has_chapters
        from mcommon import label, iso_dur
        self.assertTrue(has_chapters('x\n0:00 Intro\n1:10 A\n12:30 B'))
        self.assertFalse(has_chapters('1:10 A\n2:00 B\n3:00 C'))
        self.assertEqual(label(5, 2, 4), 'cao')
        self.assertEqual(iso_dur('PT1H2M3S'), 3723)

    def test_package_chapters_parse(self):
        from package_check import chapters, scan
        self.assertEqual(chapters('0:00 A\n0:51 B\n1:02:03 C')[2][0], 3723)
        self.assertTrue(any(k == 'ADVICE' for k, _ in scan('You should buy now')))


if __name__ == '__main__':
    unittest.main()
