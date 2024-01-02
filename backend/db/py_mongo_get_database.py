from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")


def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = config["DB_CONNECTION_STRING"]

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    db = client["MLPrediction"]
    # Create the database for our example (we will use the same database throughout the tutorial
    return db


#  This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    dbname = get_database()
