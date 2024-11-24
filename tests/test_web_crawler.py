import unittest
from unittest.mock import MagicMock, patch

from mantas_j_mod1_atsiskaitymas.web_crawler import crawl


class TestDataParser(unittest.TestCase):
    def test_validate_source_invalid_value(self):
        with self.assertRaises(ValueError):
            crawl(source='invalid_source')

    @patch('mantas_j_mod1_atsiskaitymas.crawler.webdriver.Chrome')
    def test_get_data_eurovaistine(self, mock_webdriver):
        mock_driver = MagicMock()
        mock_webdriver.return_value = mock_driver
        mock_driver.page_source = """
        <html>
            <a class="productCard">
                <div class="title"><span>Test</span></div>
                <div class="image"><img src="image_url_a.jpg"/></div>
                <div class="discountContainer"><div class="discount">10</div></div>
                <div class="productPrice"><span>10,99 €</span></div>
            </a>
        </html>
        """
        data = crawl(source='eurovaistine', return_format='list')

        # Expected parsed data
        expected_data = [{
            'title': 'Test',
            'img_url': 'image_url_a.jpg',
            'discounted': True,
            'price': 10.99
        }]
        self.assertEqual(data, expected_data)