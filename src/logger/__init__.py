import logging
import coloredlogs
import os
from datetime import datetime

# Define the directory for log files
LOG_DIR = "logs"
ERROR_LOG_DIR = os.path.join(os.getcwd(),LOG_DIR, "error_log")
INFO_LOG_DIR = os.path.join(os.getcwd(),LOG_DIR, "info_log")
LOG_DIR_PATH = os.path.join(os.getcwd(), LOG_DIR)

os.makedirs(ERROR_LOG_DIR, exist_ok=True)
os.makedirs(INFO_LOG_DIR, exist_ok=True)
os.makedirs(LOG_DIR_PATH, exist_ok=True)



# Generate a timestamp for the log file name
CURRENT_TIME_STAMP = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
ERROR_FILE_NAME = f"Error_log_{CURRENT_TIME_STAMP}.log"
INFO_FILE_NAME = f"Info_log_{CURRENT_TIME_STAMP}.log"

# LOG_FILE_PATH = os.path.join(LOG_DIR_PATH, FILE_NAME)
info_log_file = os.path.join(INFO_LOG_DIR, INFO_FILE_NAME)
error_log_file = os.path.join(ERROR_LOG_DIR, ERROR_FILE_NAME)


class InfoFilter(logging.Filter):
    """Filter for allowing only INFO level logs."""
    def filter(self, record):
        return record.levelno == logging.INFO

class Logger:
    def __init__(self, logger_name=__name__):
        self.logger_name = logger_name
        
    def CreateLogger(self):
        # Create a logger object
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.DEBUG)
        
        # Create a file handler that will be opened only when needed
        info_handler = logging.FileHandler(info_log_file, mode='w', delay=True)
        error_handler = logging.FileHandler(error_log_file, mode='w', delay=True)
        
        # Set levels and add filters
        info_handler.setLevel(logging.INFO)
        error_handler.setLevel(logging.ERROR)
        
        info_handler.addFilter(InfoFilter())  # Only INFO logs
        
        # Create a formatter for the file handlers
        file_formatter = logging.Formatter(
            "[%(asctime)s] - %(name)s - %(levelname)s - %(message)s"
        )
        
        info_handler.setFormatter(file_formatter)
        error_handler.setFormatter(file_formatter)
        
        # Add the handlers to the logger
        logger.addHandler(info_handler)
        logger.addHandler(error_handler)
        
        # Install coloredlogs for colored output in the console
        coloredlogs.install(
            level="DEBUG",
            logger=logger,
        )
        
        return logger