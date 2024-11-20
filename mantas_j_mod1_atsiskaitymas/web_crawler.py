def crawl(source = 'eurovaistine', timeout = 60, return_format = 'json'):
    match source:
        case 'eurovaistine':
            return __crawl_eurovaistine()
        case 'benu':
            return __crawl_benu()
        case _:
            raise ValueError


def __crawl_eurovaistine():
    return 'eurovaistine'

def __crawl_benu():
    return 'benu'