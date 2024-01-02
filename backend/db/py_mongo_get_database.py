import os

from pymongo import MongoClient

# isProd = os.getenv('PRODUCTION', None)

# if not (isProd):
#     from dotenv import load_dotenv
#     load_dotenv()


def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    db = client["MLPrediction"]
    # Create the database for our example (we will use the same database throughout the tutorial
    return db
