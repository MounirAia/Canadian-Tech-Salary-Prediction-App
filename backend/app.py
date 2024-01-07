import os

from db.gateway.CollectionCanada import CollectionCanada
from ml.CanadaSalaryMLModel import CanadaSalaryMLModel
from quart import Quart, jsonify, request
from quart_cors import cors as CORS

# Loading the environment variables [choose between production var or dev var(comming from .env file)]
isProd = os.getenv('PRODUCTION', None)
if not (isProd):
    from dotenv import load_dotenv
    load_dotenv()

# Setting up the Quart app
app = Quart(__name__)
# To prevent flask from ordering the json keys returned by jsonify
app.json.sort_keys = False
CORS(app, allow_origin=[os.getenv("ALLOWED_DOMAINS")])


@app.route("/api/index")
async def canada_info():
    obj = CollectionCanada.GetColumnsAndUniqueValues()

    return jsonify(obj)


@app.route("/api/salary", methods=['POST'])
async def salary_info():
    # Create the queries and build the object
    # Then refactor using motor, to leverage async

    data = await request.get_json()
    res = {}
    res["overview"] = {}
    res["dashboard"] = {}
    # Overview:
    # 1) Get the Annual Salary Info and the Hourly Salary Info predicted by the model
    salaries = CanadaSalaryMLModel.predict(data)
    res["overview"]["userSalary"] = salaries

    # 2) Get the Average yearly and hourly salary for the given city (any role) and experience (user's experience)
    averageSalaryForCity = CollectionCanada.GetAverageSalaryForCity(
        {"City": data["City"], "Experience": data["Experience"]})
    res["overview"]["averageSalaryForCity"] = averageSalaryForCity

    # Dashboard: For each category, add a highlighted value for the frontend to know which one is selected

    # 1) Get the salary info per experience for the given role and city
    res["dashboard"]["AverageSalaryPerExperience"] = CollectionCanada.GetAverageSalaryForACityAndTitleByExperience(
        {"City": data["City"], "Title": data["Title"], "Experience": data["Experience"]})

    # 2) Get the average salary for the given role per city
    res["dashboard"]["AverageSalaryPerCity"] = CollectionCanada.GetAverageSalaryForATitleByCity(
        {"Title": data["Title"], "City": data["City"]})

    # 3) Get the average salary per role for the given city
    res["dashboard"]["AverageSalaryPerTitle"] = CollectionCanada.GetAverageSalaryForACityByTitle(
        {"Title": data["Title"], "City": data["City"]})

    # 4) Get the salary info for a city some industry
    res["dashboard"]["AverageSalaryPerIndustry"] = CollectionCanada.GetAverageSalaryForACityByIndustry(
        {"City": data["City"], "Industry": data["Industry"]})

    return jsonify(res)
