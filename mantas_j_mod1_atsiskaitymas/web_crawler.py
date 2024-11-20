import requests

def crawl(source = 'eurovaistine', timeout = 60, return_format = 'json'):
    match source:
        case 'eurovaistine':
            return __crawl_eurovaistine(timeout)
        case 'benu':
            return __crawl_benu()
        case _:
            raise ValueError


def __crawl_eurovaistine(response_timeout):
    response = requests.get('https://www.eurovaistine.lt/vaistai-nereceptiniai', timeout=response_timeout)
    return response.text

def __crawl_benu():
    return 'benu'