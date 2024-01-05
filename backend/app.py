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
# To prevent flask from ordering the json keys returned by jsonify
app.json.sort_keys = False
CORS(app, origins=[os.getenv("ALLOWED_DOMAINS")])


@app.route("/api/index")
def canada_info():
    obj = CollectionCanada.GetColumnsAndUniqueValues()

    return jsonify(obj)


@app.route("/api/salary", methods=['POST'])
def salary_info():
    # Create the queries and build the object
    #  Then refactor using motor, to leverage async

    data = request.get_json()
    res = {}
    res["overview"] = {}
    res["dashboard"] = {}
    # Overview:
    # 1) Get the Annual Salary Info and the Hourly Salary Info
    salaries = CanadaSalaryMLModel.predict(data)
    res["overview"]["userSalary"] = salaries

    # 2) Get the Average yearly and hourly salary for the given city (any role) and experience
    averageSalaryForCity = CollectionCanada.GetAverageSalaryForCity(
        {"City": data["City"], "Experience": data["Experience"]})
    res["overview"]["averageSalaryForCity"] = averageSalaryForCity

    # Dashboard: For each category, add a highlighted value for the frontend to know which one is selected
    # 1) Get the salary info per experience
    res["dashboard"]["AverageSalaryPerExperience"] = CollectionCanada.GetAverageSalaryForACityAndTitleByExperience(
        {"City": data["City"], "Title": data["Title"]})

    print(res["dashboard"]["AverageSalaryPerExperience"])

    # 2) Get the average salary for the given role per city
    # 2.1) Limit for certain Canadian cities [Toronto, Vancouver, Montreal, Ottawa, Calgary, Edmonton, Quebec City, Winnipeg, Hamilton, Kitchener]
    # 3) Get the average salary per role in the city
    # 3.1) Limit for certain role [full stack, front end, back end, QA, devops, datascientist]
    # 4) Get the salary info for some industry

    return jsonify(res)
