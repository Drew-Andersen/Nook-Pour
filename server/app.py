from flask import Flask, jsonify, request
from flask_cors import CORS 
from actions import *


app = Flask(__name__)
CORS(app)

drinks = [
    {"id": 1, "name": "Margarita", "ingredients": ["Tequila", "Triple Sec", "Lime Juice"]},
    {"id": 2, "name": "Old Fashion", "ingredients": ["Whiskey", "Bitters", "Simple Syrup"]},
]

# @app.route("/")
# def home():
#     return jsonify({"message": "Welcome to the Nook & Pour API!"})

# @app.route("/api/drinks", methods=["GET"])
# def get_drinks():
#     return jsonify(drinks)

# @app.route("/api/drinks", methods=["POST"])
# def add_drink():
#     data = request.get_json()
#     drinks.append(data)
#     return jsonify({"message": "Drink added successfully!"}), 201

# if __name__ == "__main__":
#     app.run(debug=True)

@app.route('/testdbconnection')
def testdb():    
    if cursor:
        return "Connect to DB was successful"
    else:
        return "DB connection failure"
    

@app.route('/addcontenttype',methods=["POST"])
def addcontenttype():
    data = request.get_json()
    contentTypeID = data.get("contenttypeid")
    contentTypeName = data.get("contenttypename")
    return addNewContentType(contentTypeID,contentTypeName)

@app.route("/addcontent",methods=["POST"])
def addcontent():
    data = request.get_json()
    contentName = data.get("contentname")
    contentType = data.get("contenttype")
    return addNewContent(contentName,contentType)

@app.route('/adddrink',methods=["POST"])
def adddrink():
    data = request.get_json()
    drinkName = data.get("drinkname")
    return addDrink(drinkName)

@app.route("/addformula",methods=["POST"])
def addformula():
    data = request.get_json()
    drinkName = data.get("drinkname")
    contentName = data.get("contentname")
    quantity = data.get("quantity")
    return addFormula(drinkName,contentName,quantity)

@app.route("/getallformulas",methods=["GET"])
def getallformulas():
    return getAllFormulas()

@app.route("/getformula",methods=["GET"])
def getformula():
    data = request.get_json()
    drinkName = data.get("drinkname")
    return(getFormula(drinkName))


if __name__ == __name__:
    app.run(host='0.0.0.0',debug=True)