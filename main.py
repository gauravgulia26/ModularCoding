from src.logger import Logger
from src.exceptions import CustomException
logger = Logger("Setup Logger")

logger = logger.CreateLogger()

logger.info("Script is Starting")

try:
    a = int(input())
    if a == 10:
        raise ValueError("10 is not allowed")
    else:
        print(a)
except ValueError as e:
    message = type(e).__name__
    CustomException(message=message).CreateException()
