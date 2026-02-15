from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Sample Data to get Everything connected
drinks = [
    {
        'id': "margarita",
        'name': "Margarita",
        'icon': "🥃",
        'image': '/images/Marg-img.png',
        'ingredients': ["Tequila", "Triple Sec", "Lime Juice"],
        'instructions': [
            "Combine ingredients in a shaker with ice.",
            "Shake well and strain into a chilled glass.",
            "Garnish with a lime wedge.",
        ],
    },
    {
        'id': "martini",
        'name': "Martini",
        'icon': "🍸",
        'image': '/images/Martini-img.png',
        'ingredients': ["Gin", "Dry Vermouth"],
        'instructions': [
            "Stir with ice and strain into a chilled martini glass.", 
            "Garnish with an olive."
        ],
    },
    {
        'id': "mojito",
        'name': "Mojito",
        'icon': "🍹",
        'image': '/images/Mojito-img.png',
        'ingredients': ["Rum", "Lime Juice", "Simple Syrup", "Club Soda"],
        'instructions': [
            "Muddle mint and lime with simple syrup.",
            "Add rum and ice, top with club soda.",
            "Garnish with a mint sprig.",
        ],
    },
    {
        'id': "whiskey_sour",
        'name': "Whiskey Sour",
        'icon': "🥃",
        'image': '/images/Whiskey-Sour-img.png',
        'ingredients': ["Whiskey", "Lemon Juice", "Simple Syrup"],
        'instructions': ["Shake with ice and strain into a rocks glass.", "Garnish with a cherry."],
    },
    {
        'id': "old_fashion",
        'name': "Old Fashion",
        'icon': "🥃",
        'image': '/images/Old-Fashion-img.png',
        'ingredients': ["Whiskey", "Angostura Bitters", "Simple Syrup"],
        'instructions': [
            "Add whiskey, bitters, and simple syrup into a mixing glass with ice.",
            "Stir until well-chilled.",
            "Strain into a rocks glass over one large ice cube.",
            "Optional: Garnish with an orange peel twist.",
        ],
    },
    {
        'id': "espresso_martini",
        'name': "Espresso Martini",
        'icon': "🍸",
        'image': '/images/Espresso-Martini-img.png',
        'ingredients': ["Vodka", "Coffee Liqueur", "Espresso", "Simple Syrup"],
        'instructions': [
            "Shake all ingredients with ice until frothy.",
            "Strain into a chilled martini glass.",
            "Garnish with coffee beans.",
        ],
    },
    {
        'id': "pumpkin_spice_white_russian",
        'name': "Pumpkin Spice White Russian",
        'icon': "🥃",
        'image': '/images/Pumpkin-Spice-WR.png',
        'ingredients': ["Vodka", "Coffee Liqueur", "Pumpkin Puree", "Heavy Cream"],
        'instructions': [
            "Optional: Rim a rocks glass with crushed graham crackers and pumpkin spice.",
            "Fill the glass with ice.",
            "Add vodka and coffee liqueur.",
            "Pour in pumpkin mixture (pumpkin puree and heavy cream).",
            "Stir gently to combine.",
            "Optional: Top with freshly ground cinnamon.",
        ],
    },
]

@app.route("/")
def root():
    return "THIS IS MY FLASK SERVER"


@app.route('/api/drinks', methods=['GET'])
def get_drinks():
    return jsonify(drinks)

@app.route("/api/drinks/<drink_id>", methods=["GET"])
def get_drink(drink_id):
    for drink in drinks:
        if drink['id'] == drink_id:
            return jsonify(drink)
    return jsonify({'error:': "Drink not found"}), 404


# Route Built for testing
@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Server is working"})

if __name__ == "__main__":
    app.run(debug=True)
