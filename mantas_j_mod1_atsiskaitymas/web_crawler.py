import requests

def crawl(source = 'eurovaistine', timeout = 60, return_format = 'json'):
    match source:
        case 'eurovaistine':
            response_data = __get_web_data_as_text('https://www.eurovaistine.lt/vaistai-nereceptiniai', timeout)
            data = __parse_eurovaistine_data(response_data)
            return None
        case 'benu':
            response_data = __get_web_data_as_text('https://www.benu.lt/gydymas-ir-profilaktika', timeout)
            data = parse_benu_data(response_data)
            return None
        case _:
            raise ValueError

def __get_web_data_as_text(url, response_timeout):
    response = requests.get(url, timeout=response_timeout)
    return response.text

def __parse_eurovaistine_data(data):
    return data

def parse_benu_data(data):
    return data