import asyncio
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
    obj = await CollectionCanada.GetColumnsAndUniqueValues()

    return jsonify(obj)


@app.route("/api/salary", methods=['POST'])
async def salary_info():
    data = await request.get_json()
    res = {}
    res["overview"] = {}
    res["dashboard"] = {}

    overviewAverageSalaryForCity, dashboardAverageSalaryPerExperience, dashboardAverageSalaryPerCity, dashboardAverageSalaryPerTitle, dashboardAverageSalaryPerIndustry = await asyncio.gather(
        CollectionCanada.GetAverageSalaryForCity(
            {"City": data["City"], "Experience": data["Experience"]}),
        CollectionCanada.GetAverageSalaryForACityAndTitleByExperience(
            {"City": data["City"], "Title": data["Title"]}),
        CollectionCanada.GetAverageSalaryForATitleByCity(
            {"Title": data["Title"], "City": data["City"]}),
        CollectionCanada.GetAverageSalaryForACityByTitle(
            {"Title": data["Title"], "City": data["City"]}),
        CollectionCanada.GetAverageSalaryForACityByIndustry(
            {"City": data["City"], "Industry": data["Industry"]})
    )

    salaries = CanadaSalaryMLModel.predict(data)
    # Send back the requested data (useful for the frontend)
    res["user"] = data

    # Overview:

    # 1) Get the Annual Salary Info and the Hourly Salary Info predicted by the model
    res["overview"]["userSalary"] = salaries

    # 2) Get the Average yearly and hourly salary for the given city (any role) and experience (user's experience)
    res["overview"]["averageSalaryForCity"] = overviewAverageSalaryForCity

    # Dashboard: For each category, add a highlighted value for the frontend to know which one the user should compare with

    # 1) Get the salary info per experience for the given role and city
    res["dashboard"]["AverageSalaryPerExperience"] = dashboardAverageSalaryPerExperience

    # 2) Get the average salary for the given role per city
    res["dashboard"]["AverageSalaryPerCity"] = dashboardAverageSalaryPerCity

    # 3) Get the average salary per role for the given city
    res["dashboard"]["AverageSalaryPerTitle"] = dashboardAverageSalaryPerTitle

    # 4) Get the salary info for a city some industry
    res["dashboard"]["AverageSalaryPerIndustry"] = dashboardAverageSalaryPerIndustry

    return jsonify(res)
