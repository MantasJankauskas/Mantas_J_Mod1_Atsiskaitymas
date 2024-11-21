import unittest
from mantas_j_mod1_atsiskaitymas.crawler import Crawl

class TestDataParser(unittest.TestCase):
    def test_validate_source_invalid_value(self):
        with self.assertRaises(ValueError):
            Crawl('invalid_source')

    def test_validate_source_valid_value(self):
        try:
            Crawl('eurovaistine')
            Crawl('apotheka')
        except:
            self.fail('An exception was raised.')