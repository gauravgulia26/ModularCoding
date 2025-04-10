from pymongo import MongoClient
from src.exceptions import CustomException


def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://root:example@localhost:27017/?authSource=admin"

    # CONNECTION_STRING = "mongodb://root:example@localhost:27017/myFirstDatabase"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    try:
        client = MongoClient(CONNECTION_STRING)
    except Exception as e:
        err = CustomException(message=e)
        err.CreateException()
    else:
        print("Connection Established")

    # Create the database for our example (we will use the same database throughout the tutorial
    print('DataBase Created')
    return client["user_shopping_list"]


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    dbname = get_database()
