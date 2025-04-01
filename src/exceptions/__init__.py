import sys
from src.logger import Logger

logger = Logger("Exception Logger").CreateLogger()

class CustomException(Exception):
    def __init__(self, message):
        self.message = message

    def CreateException(self):
        _, _, exc_tb = sys.exc_info()
        if exc_tb:
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            logger.error(f"{self.message} Occured in {file_name} at {line_number}")
        else:
            logger.error("Traceback is not availble")
