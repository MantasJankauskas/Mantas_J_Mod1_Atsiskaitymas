class DataParser:
    accepted_formats = {'json'}

    def __init__(self, return_format: str = 'json'):
        self.return_format = return_format
        self.__validate_format()


    def __validate_format(self):
        if self.return_format not in self.accepted_formats:
            raise ValueError(f"Invalid return_format: '{self.return_format}'. Accepted formats are: {self.accepted_formats}")