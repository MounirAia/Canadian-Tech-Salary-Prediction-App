import json

from flask import Flask
from py_mongo_get_database import CollectionCanada

app = Flask(__name__)


@app.route("/api/canada-columns")
def canada_info():
    columns = CollectionCanada.GetColumns()
    res = {"columns": columns}

    return json.dumps(res)
