
from flask import Flask, json, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
def checkPostedData(postedData, functionName):
    if(functionName == "add"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif(functionName == "subtract"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif(functionName == "multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif(functionName == "divide"):
        if "x" not in postedData or "y" not in postedData or postedData["y"] != 0:
            return 301
        else:
            return 200    

class Add(Resource):
    def post(self):

        postedData = request.get_json()

        statusCode = checkPostedData(postedData, "add")
        if (statusCode != 200):
            retJson = {
                "Message": "An error happened",
                "Status Code" : statusCode
            }
            return retJson
        
        x = postedData["x"]
        y = postedData['y']
        x = int(x)
        y = int(y)
        ret = x + y
        retMap = {
            "Message": ret,
            "Status Code" : 200
        }

        return retMap

class Subtract(Resource):
    def post(self):

        postedData = request.get_json()

        statusCode = checkPostedData(postedData, "subtract")
        if (statusCode != 200):
            retJson = {
                "Message": "An error happened",
                "Status Code" : statusCode
            }
            return retJson
        
        x = postedData["x"]
        y = postedData['y']
        x = int(x)
        y = int(y)
        ret = x - y
        retMap = {
            "Message": ret,
            "Status Code" : 200
        }

        return retMap
class Multiply(Resource):
    def post(self):

        postedData = request.get_json()

        statusCode = checkPostedData(postedData, "multiply")
        if (statusCode != 200):
            retJson = {
                "Message": "An error happened",
                "Status Code" : statusCode
            }
            return retJson
        
        x = postedData["x"]
        y = postedData['y']
        x = int(x)
        y = int(y)
        ret = x * y
        retMap = {
            "Message": ret,
            "Status Code" : 200
        }

        return retMap
class Divide(Resource):
    def post(self):
        postedData = request.get_json()
        statusCode = checkPostedData(postedData, "divide")
        if (statusCode != 200):
            retJson = {
                "Message": "An error happened",
                    "Status Code" : statusCode
            }
            return retJson
        x = postedData["x"]
        y = postedData['y']
        x = int(x)
        y = int(y)
        ret = x / y
        retMap = {
            "Message": ret,
            "Status Code" : 200
        }
        return retMap

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")
@app.route('/')
def hello_world():
    return "Hello World!"

if __name__=="__main__":
    app.rund(debug = True)