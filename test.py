import os
os.system("python -m flask run")
from flask import Flask

app = Flask("test")

@app.route("/welcome")
def welcome():
    return "welcome to the flask"
@app.route("/data")
def data():
    return "this is data we have"