import os

from pymongo import MongoClient

# If you want to run this file alone, uncomment the following lines

# isProd = os.getenv('PRODUCTION', None)

# if not (isProd):
#     from dotenv import load_dotenv
#     load_dotenv()


def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")
    databaseName = "SalaryPrediction"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    db = client[databaseName]
    # Create the database for our example (we will use the same database throughout the tutorial
    return db
