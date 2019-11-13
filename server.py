from flask import Flask,redirect,escape
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json
import time

# instantiate app
app = Flask(__name__)

# load env file
load_dotenv()

# get env variables
DB_URI = os.getenv("DB_URI")
DB_NAME = os.getenv("DB_NAME")

# setup client
client = MongoClient(DB_URI)
db = client[DB_NAME]

@app.route("/")
def hello():
    return "hello there"

@app.route("/getData")
def getData():
    try:
        data = db.data.find_one()

        if data == None:
            return "no data at this moment"
        else:
            print(data)
            timestamp = data['timestamp']
            t_2 = time.time()
            print(t_2)
            print(t_2-timestamp)

            return data

    except:
        return "some error occured"