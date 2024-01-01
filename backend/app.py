from dotenv import dotenv_values
from flask import Flask

config = dotenv_values(".env")
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h2>Hello, World!</h2>"
