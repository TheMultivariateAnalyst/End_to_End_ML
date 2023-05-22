import sys
from logger import logging


logging.basicConfig(filename='05_15_2023_12_46_20.log', level=logging.INFO)

def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in Python script: {0}, Line number: {1}, Error message: {2}".format(file_name, line_number, str(error))

    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail):
        super().__init__(error)
        self.error_message = error_message_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message



