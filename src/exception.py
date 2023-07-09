import sys 
from src.logger import logging

def error_message_detail(e,ed:sys):
    _,_,exc_tb = ed.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error Script name [{0}] line no [{1}] erroe message [{2}]".format(file_name,exc_tb.tb_lineno,str(e))
    return error_message

class CustomException(Exception):
    def __init__(self, e,ed:sys):
        super().__init__(e)
        self.e = error_message_detail(e,ed)

    def __str__(self):
        return self.e