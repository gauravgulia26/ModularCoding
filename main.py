from src.logger import Logger
from src.exceptions import CustomException
from src.visualization import Visualiser
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

visuals = Visualiser("/home/gaurav/Documents/ModularCoding/data/raw/UcdpPrioConflict_v24_1.csv")

print(visuals.GetShape())
