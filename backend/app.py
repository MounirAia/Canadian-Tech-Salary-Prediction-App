import os

from db.gateway.CollectionCanada import CollectionCanada
from flask import Flask, jsonify, request
from flask_cors import CORS
from ml.CanadaSalaryMLModel import CanadaSalaryMLModel

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

    return jsonify(obj)


@app.route("/api/salary", methods=['POST'])
def salary_info():
    data = request.get_json()

    salaries = CanadaSalaryMLModel.predict(data)

    return jsonify(salaries)
