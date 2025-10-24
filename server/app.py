from flask import Flask, jsonify, request
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

drinks = [
    {"id": 1, "name": "Margarita", "ingredients": ["Tequila", "Triple Sec", "Lime Juice"]},
    {"id": 2, "name": "Old Fashion", "ingredients": ["Whiskey", "Bitters", "Simple Syrup"]},
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Nook & Pour API!"})

@app.route("/api/drinks", methods=["GET"])
def get_drinks():
    return jsonify(drinks)

@app.route("/api/drinks", methods=["POST"])
def add_drink():
    data = request.get_json()
    drinks.append(data)
    return jsonify({"message": "Drink added successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True)