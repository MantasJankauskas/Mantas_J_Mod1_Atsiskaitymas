from lxml.etree import HTML
from selenium import webdriver
from mantas_j_mod1_atsiskaitymas.data_parser import DataParser

def crawl(source: str = 'eurovaistine', timeout: int = 60, return_format: str = 'json'):
    match source:
        case 'eurovaistine':
            response_data = __get_web_data_as_text('https://www.eurovaistine.lt/vaistai-nereceptiniai', timeout)
            data = __parse_eurovaistine_data(response_data)
            parsed_data = DataParser().return_in_format(data, return_format)
            return parsed_data
        case 'apotheka':
            response_data = __get_web_data_as_text('https://www.apotheka.lt/prekes/nereceptiniai-vaistai', timeout)
            data = __parse_apotheka_data(response_data)
            parsed_data = DataParser().return_in_format(data, return_format)
            return parsed_data
        case _:
            raise ValueError(f"Invalid source: '{source}'.")


def __get_web_data_as_text(url: str, response_timeout: int) -> HTML:
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(response_timeout)
    html_content = driver.page_source
    return HTML(html_content)


def __parse_eurovaistine_data(data: HTML) -> list[dict[str, bool]]:
    drugs_cards = data.xpath("//a[contains(@class, 'productCard')]")

    return [{
        'title': ''.join(drug.xpath(".//div[@class='title']/span/text()")).strip(),
        'img_url': drug.xpath(".//div[contains(@class, 'image')]//img/@src"),
        'discounted': bool(drug.xpath(".//div[contains(@class, 'discountContainer')]//div[contains(@class, 'discount')]/text()")),
        'price': ''.join(drug.xpath(".//div[contains(@class, 'productPrice')]/span/text()")).strip()[:-2]
    } for drug in drugs_cards]


def __parse_apotheka_data(data: HTML) -> list[dict[str, bool]]:
    drugs_cards = data.xpath("//div[@class='box-product']")

    return [{
        'title': ''.join(drug.xpath(".//div[@class='box-product__title']/text()")).strip(),
        'img_url': drug.xpath(".//div[contains(@class, 'box-product__image')]//img/@src"),
        'discounted': bool(drug.xpath(".//div[contains(@class, 'discountContainer')]//div[contains(@class, 'discount')]/text()")),
        'price': ''.join(drug.xpath(".//span[@class='product-pricing__price-number']/text()")).strip()[:-2]
    } for drug in drugs_cards]
