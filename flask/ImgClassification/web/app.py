from flask import Flask, request
from flask_restful import API, Resource
from pymongo import MongoClient
import bcrypt
import numpy
import requests
import subprocess
import json

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.ImageRecognition
users = db["Users"]

def UserExist(username):
    if users.find({"Username" : username}).count() ==0:
        return False
    else:
        return True
        
class Register(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData["password"]

        if UserExist(username):
            retJson = {
                "status" :301,(
                "msg" : "Invalid Username"
            }

            return retJson
        
        hashedPw = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
        users.insert({
            "Username" : username,
            "Password" : hashedPw,
            "Tokens": 10,
        })

        retJson = {
            "status" : 200,
            "msg" : "You successfully signed up for this API"
        }

        return retJson
