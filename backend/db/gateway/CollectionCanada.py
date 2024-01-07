import re
from typing import Dict

from db.get_database import get_database
from ml.CanadaSalaryMLModel import CanadaSalaryMLModel


# util function to extract the first number from a string
def _extract_first_number(s):
    # Use regular expression to find the first number in the string
    match = re.search(r'[0-9]*,?[0-9]*', s)
    if (match):
        return int(match.group().replace(',', ''))
    else:
        return 0


class CollectionCanada:
    CollectionName = "Canada"
    _columnsAndDistinctValues = None

    @staticmethod
    def _getCollection():
        dbname = get_database()
        collection = dbname[CollectionCanada.CollectionName]
        return collection

    @staticmethod
    async def GetColumns():
        collection = CollectionCanada._getCollection()
        element = await collection.find_one()
        return list(element.keys())

    @staticmethod
    async def GetColumnsAndUniqueValues():
        if (CollectionCanada._columnsAndDistinctValues != None):
            return CollectionCanada._columnsAndDistinctValues

        collection = CollectionCanada._getCollection()
        columns = await CollectionCanada.GetColumns()
        values_to_remove = ["_id", "Salary"]
        columns = list(filter(lambda x: x not in values_to_remove, columns))
        CollectionCanada._columnsAndDistinctValues = {}

        for column in columns:
            distinctValues = list(await collection.distinct(column))
            if (column == "Company Size" or column == "Experience"):
                # Sort by the first number in the string
                distinctValues = sorted(
                    distinctValues, key=_extract_first_number
                )
            else:
                # Alphabetic sorting
                distinctValues = sorted(distinctValues)

            CollectionCanada._columnsAndDistinctValues[column] = distinctValues

        return CollectionCanada._columnsAndDistinctValues

    @staticmethod
    async def GetAverageSalaryForCity(parameters: Dict[str, str]):
        collection = CollectionCanada._getCollection()

        output = {"yearly": None, "hourly": None}

        City = parameters["City"]
        Experience = parameters["Experience"]

        pipeline = [
            {
                '$match': {
                    'City': City
                }
            }, {
                '$match': {
                    'Experience': Experience
                }
            }, {
                '$group': {
                    '_id': None,
                    'AverageSalary': {
                        '$avg': '$Salary'
                    }
                }
            }
        ]

        cursor = collection.aggregate(pipeline)
        dbOutput = await cursor.to_list(length=None)

        if (len(dbOutput) > 0):
            yearly = dbOutput[0]["AverageSalary"]
            hourly = CanadaSalaryMLModel.ComputeHourlySalary(yearly)
            output = {"yearly": round(yearly, 2), "hourly": round(hourly, 2)}

        return output

    @staticmethod
    async def GetAverageSalaryForACityAndTitleByExperience(parameters: Dict[str, str]):
        # Create store the schema of the object, like the columns and all the unique values the class level as a static

        collection = CollectionCanada._getCollection()

        City = parameters["City"]
        Title = parameters["Title"]
        Experience = parameters["Experience"]

        output = {}
        uniqueValuesOfExperienceColumns = (await CollectionCanada.GetColumnsAndUniqueValues())["Experience"]

        for category in uniqueValuesOfExperienceColumns:
            output[category] = None

        pipeline = [
            {
                '$match': {
                    'Title': Title
                }
            }, {
                '$match': {
                    'City': City
                }
            }, {
                '$group': {
                    '_id': '$Experience',
                    'AverageSalary': {
                        '$avg': '$Salary'
                    }
                }
            }
        ]

        cursor = collection.aggregate(pipeline)
        dbOutput = await cursor.to_list(length=None)

        for item in dbOutput:
            yearly = item["AverageSalary"]
            hourly = CanadaSalaryMLModel.ComputeHourlySalary(yearly)
            output[item["_id"]] = {"yearly": round(
                yearly, 2), "hourly": round(hourly, 2)}

        output["user"] = Experience

        return output

    @staticmethod
    async def GetAverageSalaryForATitleByCity(parameters: Dict[str, str]):
        # Return a limited number of records

        collection = CollectionCanada._getCollection()

        Title = parameters["Title"]
        City = parameters["City"]

        output = {}
        indexOfUserCity = -1
        maxRecordLength = 11

        pipeline = [
            {
                '$match': {
                    'Title': Title
                }
            }, {
                '$group': {
                    '_id': '$City',
                    'AverageSalary': {
                        '$avg': '$Salary'
                    }
                }
            }, {
                '$sort': {
                    'AverageSalary': -1
                }
            }
        ]

        cursor = collection.aggregate(pipeline)
        dbOutput = await cursor.to_list(length=None)

        for index, item in enumerate(dbOutput):
            if (item["_id"] == City):
                indexOfUserCity = index
                yearly = item["AverageSalary"]
                output[item["_id"]] = round(yearly, 2)
                output["user"] = item["_id"]

        if indexOfUserCity == -1:
            maxIndex = maxRecordLength if len(
                dbOutput) >= maxRecordLength else len(dbOutput)
            for index, item in enumerate(dbOutput[:maxIndex]):
                yearly = item["AverageSalary"]
                output[item["_id"]] = round(yearly, 2)
        else:
            for index, item in enumerate(dbOutput):
                if len(output) >= maxRecordLength:
                    break

                if (index == indexOfUserCity):
                    continue
                yearly = item["AverageSalary"]
                output[item["_id"]] = round(yearly, 2)

        return output

    @staticmethod
    async def GetAverageSalaryForACityByTitle(parameters: Dict[str, str]):
        # Return a limited number of records

        collection = CollectionCanada._getCollection()

        City = parameters["City"]
        Title = parameters["Title"]

        output = {}
        indexOfUserTitle = -1
        maxRecordLength = 11

        pipeline = [
            {
                '$match': {
                    'City': City
                }
            }, {
                '$group': {
                    '_id': '$Title',
                    'AverageSalary': {
                        '$avg': '$Salary'
                    }
                }
            }, {
                '$sort': {
                    'AverageSalary': -1
                }
            }
        ]

        cursor = collection.aggregate(pipeline)
        dbOutput = await cursor.to_list(length=None)

        for index, item in enumerate(dbOutput):
            if (item["_id"] == Title):
                indexOfUserTitle = index
                yearly = item["AverageSalary"]
                output[item["_id"]] = round(yearly, 2)
                output["user"] = item["_id"]

        if indexOfUserTitle == -1:
            maxIndex = maxRecordLength if len(
                dbOutput) >= maxRecordLength else len(dbOutput)

            for index, item in enumerate(dbOutput[:maxIndex]):
                yearly = item["AverageSalary"]
                output[item["_id"]] = round(yearly, 2)
        else:
            for index, item in enumerate(dbOutput):
                if len(output) >= maxRecordLength:
                    break

                if (index == indexOfUserTitle):
                    continue

                yearly = item["AverageSalary"]
                output[item["_id"]] = round(yearly, 2)

        return output

    @staticmethod
    async def GetAverageSalaryForACityByIndustry(parameters: Dict[str, str]):
        # Return a limited number of records

        collection = CollectionCanada._getCollection()

        City = parameters["City"]
        Industry = parameters["Industry"]

        output = {}
        indexOfUserTitle = -1
        maxRecordLength = 5

        pipeline = [
            {
                '$match': {
                    'City': City
                }
            }, {
                '$group': {
                    '_id': '$Industry',
                    'AverageSalary': {
                        '$avg': '$Salary'
                    }
                }
            }, {
                '$sort': {
                    'AverageSalary': -1
                }
            }
        ]

        cursor = collection.aggregate(pipeline)
        dbOutput = await cursor.to_list(length=None)

        for index, item in enumerate(dbOutput):
            if (item["_id"] == Industry):
                indexOfUserTitle = index
                yearly = item["AverageSalary"]
                output[item["_id"]] = round(yearly, 2)
                output["user"] = item["_id"]

        if indexOfUserTitle == -1:
            maxIndex = maxRecordLength if len(
                dbOutput) >= maxRecordLength else len(dbOutput)

            for index, item in enumerate(dbOutput[:maxIndex]):
                yearly = item["AverageSalary"]
                output[item["_id"]] = round(yearly, 2)
        else:
            for index, item in enumerate(dbOutput):
                if len(output) >= maxRecordLength:
                    break

                if (index == indexOfUserTitle):
                    continue

                yearly = item["AverageSalary"]
                output[item["_id"]] = round(yearly, 2)

        return output
