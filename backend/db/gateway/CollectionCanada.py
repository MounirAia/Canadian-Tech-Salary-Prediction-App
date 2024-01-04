import re

from db.py_mongo_get_database import get_database


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

    @staticmethod
    def _getCollection():
        dbname = get_database()
        collection = dbname[CollectionCanada.CollectionName]
        return collection

    @staticmethod
    def GetColumns():
        collection = CollectionCanada._getCollection()
        return list(collection.find_one().keys())

    @staticmethod
    def GetColumnsAndUniqueValues():
        collection = CollectionCanada._getCollection()
        columns = CollectionCanada.GetColumns()
        values_to_remove = ["_id", "Salary"]
        columns = list(filter(lambda x: x not in values_to_remove, columns))
        res = {}

        for column in columns:
            distinctValues = list(collection.distinct(column))
            if (column == "Company Size" or column == "Experience"):
                # Sort by the first number in the string
                distinctValues = sorted(
                    distinctValues, key=_extract_first_number
                )
            else:
                # Alphabetic sorting
                distinctValues = sorted(list(collection.distinct(column)))

            res[column] = distinctValues

        return res
