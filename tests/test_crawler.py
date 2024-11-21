import unittest
from unittest.mock import MagicMock, patch

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

    @patch('mantas_j_mod1_atsiskaitymas.crawler.webdriver.Chrome')
    def test_get_web_data_as_text(self, mock_chrome):
        mock_driver = MagicMock()
        mock_driver.page_source = "<html><head><title>Test</title></head></html>"
        mock_chrome.return_value = mock_driver

        instance = Crawl('eurovaistine')
        result = instance._Crawl__get_web_data_as_text("https://example.com", 10)

        self.assertEqual(result.xpath("//title/text()")[0], "Test")

        mock_driver.get.assert_called_once_with("https://example.com")