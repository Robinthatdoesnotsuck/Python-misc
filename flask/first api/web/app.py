"""
Allow registration of a user
Each user gets 10 tokens
Store a sentence on our database for 1 token
Retrieve his stored sentence on the database for 1 token
"""
from flask import Flask, json, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
# Creates DB
db = client.SentencesDatabase
# Creates collection
users = db["Users"]

# functions

# first we verify the password
def verifyPw(username, password):

    hashed_pw = users.find({
        "Username" : username
    })[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def countTokens(username):
    tokens = users.find({
        "Username" : username
    })[0]["Tokens"]
    return tokens

class Register(Resource):
    def post(self):
        # Step 1 get posted data by the user
        postedData = request.get_json()

        # Get the data
        username = postedData['username']
        password = postedData['password']
        
        # we need to crypt our data
        hashed = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
        # store username and pw into the database
        users.insert({
            "Username" : username,
            "Password" : hashed,
            "Sentence" : "",
            "Tokens"   : 6
        })

        retJson = {
            "status" : 200,
            "msg" : "You successfully signed up for the API"
        }
        return retJson

class Store(Resource):
    def post(self):
        postedData = request.get_json()

        username = postedData["username"]
        password = postedData['password']
        sentence = postedData['sentence']

        # verify username and pw match
        correct_pw = verifyPw(username, password)
        if not correct_pw:
            retJson = {
                "status" : 302
            }
            return retJson
        # verify user tokens
        num_tokens = countTokens(username)
        if num_tokens <= 0:
            retJson = {
                "status" : 301
            }
            return jsonify(retJson)
        else:
            num_tokens = num_tokens -1
        # store sentences and return 2000k
        users.update({
            "Username" : username
        }, {
            "$set" : {
                    "Sentence" : sentence,
                    "Tokens": num_tokens
                    }
            })
        retJson = {
            "status": 200,
            "msg" : "Sentence saved successfully"
        }
        return retJson
    def get:
        
class Get(Resource):
    def post(self):
        getData = request.get_json()

        username = getData["username"]
        password = getData["password"]

        correct_pw = verifyPw(username, password)
        if not correct_pw:
            retJson = {
                "status" : 302
            }
            return retJson
        num_tokens = countTokens(username)
        if num_tokens <= 0:
            retJson = {
                "status" : 301
            }
            return jsonify(retJson)
        # make user api

        users.update({
            "Username" : username
        },  {
            "$set" : {
                "Tokens" : num_tokens - 1
            }
        }
        ) 
        sentence = users.find({
            "Username" : username
        })[0]["Sentence"]

        retJson = {
            "status" : 200,
            "sentence" : sentence
        }

        return retJson

api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Get, '/get')

if __name__ == "__main__":
    app.run(host = '0.0.0.0')
