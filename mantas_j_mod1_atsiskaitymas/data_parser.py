import json

class DataParser:
    accepted_formats = {'json'}
    data_to_parse = None

    def __validate_format(self, return_format):
        if return_format not in self.accepted_formats:
            raise ValueError(f"Invalid return_format: '{return_format}'. Accepted formats are: {self.accepted_formats}")

    def return_in_format(self, data: list, return_format: str = 'json'):
        self.__validate_format(return_format)
        self.data_to_parse = data

        match return_format:
            case 'json':
                return self.__return_json_format()

    def __return_json_format(self):
        return json.dumps(self.data_to_parse)