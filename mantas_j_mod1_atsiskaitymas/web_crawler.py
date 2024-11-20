from lxml.etree import HTML
from selenium import webdriver

def crawl(source: str = 'eurovaistine', timeout: int = 60, return_format: str = 'json'):
    match source:
        case 'eurovaistine':
            response_data = __get_web_data_as_text('https://www.eurovaistine.lt/vaistai-nereceptiniai', timeout)
            data = __parse_eurovaistine_data(response_data)
            return data
        case 'benu':
            response_data = __get_web_data_as_text('https://www.benu.lt/gydymas-ir-profilaktika', timeout)
            data = __parse_benu_data(response_data)
            return None
        case _:
            raise ValueError


def __get_web_data_as_text(url: str, response_timeout: int) -> HTML:
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(response_timeout)
    html_content = driver.page_source
    return HTML(html_content)


def __parse_eurovaistine_data(data: HTML) -> list[dict[str, str | bool]]:
    drugs_cards = data.xpath("//a[contains(@class, 'productCard')]")

    return [{
        'title': ''.join(drug.xpath(".//div[@class='title']/span/text()")).strip(),
        'discounted': bool(drug.xpath(".//div[contains(@class, 'discountContainer')]//div[contains(@class, 'discount')]/text()")),
        'price': ''.join(drug.xpath(".//div[contains(@class, 'productPrice')]/span/text()")).strip()[:-2]
    } for drug in drugs_cards]


def __parse_benu_data(data: HTML):
    return data
