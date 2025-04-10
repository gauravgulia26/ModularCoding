from src.logger import Logger
from src.exceptions import CustomException
from src.visualization import Visualiser
from src.components.mongodbconn.mongo import get_database

logger = Logger("Setup Logger")

logger = logger.CreateLogger()

logger.info("Script is Starting")

try:
    dbname = get_database()
    collection_name = dbname["user_1_items"]
    item_1 = {
        "_id": "U1IT00001",
        "item_name": "Blender",
        "max_discount": "10%",
        "batch_number": "RR450020FRG",
        "price": 340,
        "category": "kitchen appliance",
    }

    item_2 = {
        "_id": "U1IT00002",
        "item_name": "Egg",
        "category": "food",
        "quantity": 12,
        "price": 36,
        "item_description": "brown country eggs",
    }
    try:
        collection_name.insert_many([item_1, item_2])
    except Exception as e:
        err = CustomException(message=e)
        err.CreateException()
    else:
        logger.debug("Data Inserted !!")
except ValueError as e:
    message = type(e).__name__
    CustomException(message=message).CreateException()

visuals = Visualiser(
    "/home/gaurav/Documents/ModularCoding/data/raw/UcdpPrioConflict_v24_1.csv"
)

print(visuals.GetShape())
