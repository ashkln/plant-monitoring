# module imports
from flask import Flask, escape, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# flask app declaration
app = Flask(__name__)

# load env files and token
load_dotenv()

# get env variables
DB_URI = os.getenv(DB_URI)
DB_NAME = os.getenv(DB_NAME)

# connect to db
client = MongoClient(DB_URI)
db = client[DB_NAME]


# test route
@app.route("/")
def test():
    return "test route"

@app.route("/getdata")
def sendData():
    pass
