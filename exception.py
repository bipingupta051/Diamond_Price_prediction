import sys
from src.logger import logging

def error_message_details(error, error_details: sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number [{1}] error message [{2}]".format()
    exc_tb.tb_lineno,str(error)
    return error_message

import sys

class CustomException(Exception):
    def __init__(self, error_message: str, error_details: str):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_details = error_details
    
    def __str__(self):
        return f"{self.error_message}: {self.error_details}"

    
    
    
if __name__=="__main__":
    logging.info("Logging has started")
    
    try:
        a=1/0
    except Exception as e:
        logging.info('Devision by zero ')
        raise CustomException(e,sys)
        
    
    
