import json
import os

from db.gateway.CollectionCanada import CollectionCanada
from flask import Flask
from flask_cors import CORS

# Loading the environment variables
isProd = os.getenv('PRODUCTION', None)
if not (isProd):
    from dotenv import load_dotenv
    load_dotenv()

# Setting up the Flask app
app = Flask(__name__)
CORS(app, origins=[os.getenv("ALLOWED_DOMAINS")])


@app.route("/api/index")
def canada_info():
    obj = CollectionCanada.GetColumnsAndUniqueValues()

    return json.dumps(obj)
