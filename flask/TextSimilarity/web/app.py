from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
import spacy

app = Flask(__name__)
app = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.SimilarityDB
users = db["Users"]
def UserExist(username):
    if users.find({"Username": username}).count() == 0:
        return False
    else:
        return True

def verifyPW(username, password):
    if not UserExist(username):
        return False
    hashed_pw = users.find({
        "Username" : username
    })[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False
    
def verifyAdminPW(username, password):
    if not UserExist(username):
        return False
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
        postedData = request.get_json()

        username = postedData["username"]
        password = postedData["password"]

        if UserExist(username):
            retJson = {
                "status": 301,
                "msg" : "Username already exists"
            }
            return retJson
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        users.insert({
            "Username": username,
            "Password": hashed_pw,
            "Tokens": 6 
        })

        retJson = {
            "status" : 200,
            "msg" : "You've subscribed to the API"
        }

        return jsonify(retJson)

class Detect(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData['password']

        text1 = postedData['text1']
        text2 = postedData['text2']

        if not UserExist(username):
            retJson = {
                "status": 301,
                "msg" : "Invalid username"
            }
            return retJson
        correct_pw = verifyPW(username, password)
        if not correct_pw:
            retJson = {
                "status" : 302,
                "Invalid password"
            }
            return retJson
        
        num_tokens = countTokens(username)

        if num_tokens <= 0:
            retJson = {
                "status" : 303,
                "msg" : "not enough Tokens please refill"
            }

            return retJson
        # calculate the edit distance
        nlp = spacy.load('en_core_web_sm')
        text1 = nlp(text1)
        text2 = nlp(text2)

        # ratio is the similarity between the two texts

        ratio = text1.similarity(text2)

        retJson = {
            "status" : 200,
            "similarity ratio" : ratio,
            "msg" : "Similarity score calculated successfully"
        }
        current_tokens = countTokens(username)
        users.update({
            "Username" : username
        },{
            "$set": {
                "Tokens" : current_tokens - 1
            }
        })


class Refill():
    def post(self):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData['admin_pw']
        refillAmount = postedData['refillAmount']   

        ## validation
        if not UserExist(username):
            retJson = {
                "status": 301,
                "msg" : "Invalid username"
            }
            return retJson

        correct_pw = verifyPW(username, password)

        if not correct_pw:
            retJson = {
                "status" : 304,
                "Invalid administrator password"
            }
            return retJson

        currentTokens = countTokens(username)
        users.update({
            "Username": username
            },{
                "$set" : {
                    "Tokens": refillAmount + currentTokens
                }
            })     
        retJson = {
            "status" : 200,
            "msg" : "Refilled successfully"
        }

        return retJson

api.add_resource(Register, '/register')
api.add_resource(Detect, '/detect')
api.add_resource(Refill, '/refill')

if __name__ == "__main__":
    app.run(host = '0.0.0.0')