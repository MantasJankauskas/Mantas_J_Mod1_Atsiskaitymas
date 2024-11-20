import requests
from lxml.etree import HTML

def crawl(source: str = 'eurovaistine', timeout: int = 60, return_format:str = 'json'):
    match source:
        case 'eurovaistine':
            response_data = __get_web_data_as_text('https://www.eurovaistine.lt/vaistai-nereceptiniai', timeout)
            data = __parse_eurovaistine_data(response_data)
            return None
        case 'benu':
            response_data = __get_web_data_as_text('https://www.benu.lt/gydymas-ir-profilaktika', timeout)
            data = __parse_benu_data(response_data)
            return None
        case _:
            raise ValueError

def __get_web_data_as_text(url: str, response_timeout: int) -> HTML:
    response = requests.get(url, timeout=response_timeout)
    return HTML(response.text)

def __parse_eurovaistine_data(data: HTML):
    return data

def __parse_benu_data(data: HTML):
    return data