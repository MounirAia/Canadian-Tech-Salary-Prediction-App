import json

from db.gateway.CollectionCanada import CollectionCanada
from flask import Flask

app = Flask(__name__)


@app.route("/api/index")
def canada_info():
    obj = CollectionCanada.GetColumnsAndUniqueValues()

    return json.dumps(obj)
