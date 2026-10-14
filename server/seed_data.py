"""Each drink lists its ingredients as (name, amount, optional). Optional items
(garnishes, rims) are shown in the recipe but never stop a drink from matching.
Every ingredient name used in DRINKS must appear in INGREDIENTS.
"""

INGREDIENTS = {
    "spirit": [
        "Vodka", "Gin", "Rum", "Coconut Rum", "Spiced Rum", "Tequila", "Mezcal", 
        "Whiskey", "Rye Whiskey", "Bourbon", "Scotch", "Brandy", "Cognac", 
        "Absinthe"
    ],
    "liqueur": [
        "Triple Sec", "Coffee Liqueur", "Campari", "Dry Vermouth", "Sweet Vermouth", 
        "Aperol", "Irish Cream", "Peach Schnapps", "Elderflower Liqueur", "Blue Curaçao", 
        "Raspberry Liqueur", "Chocolate Liqueur", "Strawberry Cream Liqueur", "Prosecco"
    ],
    "mixer": [
        "Lime Juice", "Lemon Juice", "Orange Juice", "Cranberry Juice", "Simple Syrup",
        "Grenadine", "Angostura Bitters", "Club Soda", "Tonic Water", "Ginger Beer",
        "Cola", "Grapefruit Soda", "Espresso", "Heavy Cream", "Pumpkin Puree", "Pineapple Juice",
        "Grapefruit Juice", "Tomato Juice", "Coconut Cream", "Ginger Ale", "Lemon-Lime Soda", 
        "Agave Syrup", "Honey Syrup", "Orange Bitters", "Chocolate Bitters", "Milk", "Egg White",
        "Worcestershire Sauce", "Hot Sauce"
    ],
    "garnish": [
        "Mint", "Lime Wedge", "Lemon Wedge", "Lemon Twist", "Orange Slice", "Orange Peel", 
        "Pineapple Wedge", "Olive", "Cocktail Cherry", "Coffee Beans", "Salt", "Cinnamon", 
        "Celery Stalk", "Sugar", "Nutmeg", "Rosemary", "Basil", "Cucumber", "Blueberries", 
        "Strawberries", "Jalapeño"
    ],
}

DRINKS = [
    {
        "slug": "margarita", "name": "Margarita", "kind": "cocktail", "icon": "🍹",
        "glass": "Coupe or rocks", "image": "/images/Marg-img.png",
        "description": "Bright, tart and a little salty — the tequila classic.",
        "ingredients": [
            ("Tequila", "2 oz", False), ("Triple Sec", "1 oz", False),
            ("Lime Juice", "1 oz", False), ("Salt", "for the rim", True),
            ("Lime Wedge", "1", True),
        ],
        "instructions": [
            "Optional: run a lime wedge around the rim and dip it in salt.",
            "Combine tequila, triple sec and lime juice in a shaker with ice.",
            "Shake well and strain into the glass.",
            "Garnish with a lime wedge.",
        ],
    },
    {
        "slug": "martini", "name": "Martini", "kind": "cocktail", "icon": "🍸",
        "glass": "Martini", "image": "/images/Martini-img.png",
        "description": "Cold, clean and bracing. Stirred, never rushed.",
        "ingredients": [
            ("Gin", "2½ oz", False), ("Dry Vermouth", "½ oz", False), ("Olive", "1–3", True),
        ],
        "instructions": [
            "Stir gin and dry vermouth with ice for about 30 seconds.",
            "Strain into a chilled martini glass.",
            "Garnish with an olive.",
        ],
    },
    {
        "slug": "mojito", "name": "Mojito", "kind": "cocktail", "icon": "🌿",
        "glass": "Highball", "image": "/images/Mojito-img.png",
        "description": "Mint, lime and rum topped with bubbles. Summer in a glass.",
        "ingredients": [
            ("Rum", "2 oz", False), ("Lime Juice", "¾ oz", False),
            ("Simple Syrup", "½ oz", False), ("Mint", "6–8 leaves", False),
            ("Club Soda", "top", False),
        ],
        "instructions": [
            "Gently muddle mint with lime juice and simple syrup.",
            "Add rum and fill the glass with ice.",
            "Top with club soda and give it a quick stir.",
            "Garnish with a mint sprig.",
        ],
    },
    {
        "slug": "whiskey-sour", "name": "Whiskey Sour", "kind": "cocktail", "icon": "🥃",
        "glass": "Rocks", "image": "/images/Whiskey-Sour-img.png",
        "description": "Sweet, sour and warming — the perfect intro to whiskey cocktails.",
        "ingredients": [
            ("Whiskey", "2 oz", False), ("Lemon Juice", "¾ oz", False),
            ("Simple Syrup", "¾ oz", False), ("Cocktail Cherry", "1", True),
        ],
        "instructions": [
            "Shake whiskey, lemon juice and simple syrup with ice.",
            "Strain into a rocks glass over fresh ice.",
            "Garnish with a cherry.",
        ],
    },
    {
        "slug": "old-fashioned", "name": "Old Fashioned", "kind": "cocktail", "icon": "🥃",
        "glass": "Rocks", "image": "/images/Old-Fashion-img.png",
        "description": "Whiskey, a touch of sugar and bitters. Simple and timeless.",
        "ingredients": [
            ("Whiskey", "2 oz", False), ("Simple Syrup", "¼ oz", False),
            ("Angostura Bitters", "2 dashes", False), ("Orange Peel", "1 twist", True),
        ],
        "instructions": [
            "Add whiskey, bitters and simple syrup to a mixing glass with ice.",
            "Stir until well chilled.",
            "Strain into a rocks glass over one large ice cube.",
            "Optional: express an orange peel over the drink and drop it in.",
        ],
    },
    {
        "slug": "espresso-martini", "name": "Espresso Martini", "kind": "cocktail", "icon": "☕",
        "glass": "Martini or coupe", "image": "/images/Espresso-Martini-img.png",
        "description": "Rich coffee and vodka shaken until silky and foamy.",
        "ingredients": [
            ("Vodka", "2 oz", False), ("Coffee Liqueur", "½ oz", False),
            ("Espresso", "1 oz", False), ("Simple Syrup", "¼ oz", False),
            ("Coffee Beans", "3", True),
        ],
        "instructions": [
            "Shake all ingredients hard with ice until frothy.",
            "Strain into a chilled martini glass.",
            "Garnish with three coffee beans.",
        ],
    },
    {
        "slug": "pumpkin-spice-white-russian", "name": "Pumpkin Spice White Russian",
        "kind": "cocktail", "icon": "🎃", "glass": "Rocks",
        "image": "/images/Pumpkin-Spice-WR.png",
        "description": "A cozy fall twist on the White Russian.",
        "ingredients": [
            ("Vodka", "1½ oz", False), ("Coffee Liqueur", "1 oz", False),
            ("Pumpkin Puree", "1 tbsp", False), ("Heavy Cream", "1 oz", False),
            ("Cinnamon", "pinch", True),
        ],
        "instructions": [
            "Optional: rim a rocks glass with crushed graham crackers and pumpkin spice.",
            "Fill the glass with ice.",
            "Add vodka and coffee liqueur.",
            "Whisk pumpkin puree into the heavy cream, then pour it in.",
            "Stir gently to combine.",
            "Optional: top with freshly ground cinnamon.",
        ],
    },
    {
        "slug": "daiquiri", "name": "Daiquiri", "kind": "cocktail", "icon": "🍸",
        "glass": "Coupe", "image": "/images/Daiquiri-img.png",
        "description": "Rum, lime and sugar in perfect balance. Not the slushy kind.",
        "ingredients": [
            ("Rum", "2 oz", False), ("Lime Juice", "1 oz", False),
            ("Simple Syrup", "¾ oz", False), ("Lime Wedge", "1", True),
        ],
        "instructions": [
            "Shake rum, lime juice and simple syrup with ice.",
            "Strain into a chilled coupe.",
        ],
    },
    {
        "slug": "moscow-mule", "name": "Moscow Mule", "kind": "cocktail", "icon": "🫚",
        "glass": "Copper mug", "image": "/images/Moscow-Mule-img.png",
        "description": "Spicy ginger beer, vodka and lime over lots of ice.",
        "ingredients": [
            ("Vodka", "2 oz", False), ("Ginger Beer", "4 oz", False),
            ("Lime Juice", "½ oz", False), ("Lime Wedge", "1", True),
        ],
        "instructions": [
            "Fill a copper mug with ice.",
            "Add vodka and lime juice.",
            "Top with ginger beer and stir gently.",
            "Garnish with a lime wedge.",
        ],
    },
    {
        "slug": "negroni", "name": "Negroni", "kind": "cocktail", "icon": "🍊",
        "glass": "Rocks", "image": "/images/Negroni-img.png",
        "description": "Equal parts gin, Campari and sweet vermouth. Bitter and bold.",
        "ingredients": [
            ("Gin", "1 oz", False), ("Campari", "1 oz", False),
            ("Sweet Vermouth", "1 oz", False), ("Orange Peel", "1 twist", True),
        ],
        "instructions": [
            "Stir gin, Campari and sweet vermouth with ice.",
            "Strain into a rocks glass over a large ice cube.",
            "Garnish with an orange peel.",
        ],
    },
    {
        "slug": "cosmopolitan", "name": "Cosmopolitan", "kind": "cocktail", "icon": "🍸",
        "glass": "Martini", "image": "/images/Cosmopolitan-img.png",
        "description": "Pink, tart and crisp — cranberry and citrus with vodka.",
        "ingredients": [
            ("Vodka", "1½ oz", False), ("Triple Sec", "½ oz", False),
            ("Cranberry Juice", "1 oz", False), ("Lime Juice", "½ oz", False),
            ("Orange Peel", "1 twist", True),
        ],
        "instructions": [
            "Shake all ingredients with ice.",
            "Strain into a chilled martini glass.",
            "Garnish with an orange twist.",
        ],
    },
    {
        "slug": "paloma", "name": "Paloma", "kind": "cocktail", "icon": "🍹",
        "glass": "Highball", "image": "/images/Paloma-img.png",
        "description": "Tequila and grapefruit soda — Mexico's favorite highball.",
        "ingredients": [
            ("Tequila", "2 oz", False), ("Grapefruit Soda", "4 oz", False),
            ("Lime Juice", "½ oz", False), ("Salt", "pinch", True),
            ("Lime Wedge", "1", True),
        ],
        "instructions": [
            "Optional: salt the rim of a highball glass.",
            "Fill the glass with ice and add tequila and lime juice.",
            "Top with grapefruit soda and stir.",
            "Garnish with a lime wedge.",
        ],
    },
    {
        "slug": "tom-collins", "name": "Tom Collins", "kind": "cocktail", "icon": "🍋",
        "glass": "Collins", "image": "/images/Tom-Collins-img.png",
        "description": "Sparkling gin lemonade for grown-ups.",
        "ingredients": [
            ("Gin", "2 oz", False), ("Lemon Juice", "1 oz", False),
            ("Simple Syrup", "½ oz", False), ("Club Soda", "top", False),
            ("Cocktail Cherry", "1", True),
            ("Lemon Wedge", "1", True),
        ],
        "instructions": [
            "Shake gin, lemon juice and simple syrup with ice.",
            "Strain into an ice-filled collins glass.",
            "Top with club soda and garnish with a lemon wedge and a cherry.",
        ],
    },
    {
        "slug": "gin-and-tonic", "name": "Gin & Tonic", "kind": "cocktail", "icon": "🧊",
        "glass": "Highball", "image": "/images/Gin-Tonic-img.png",
        "description": "Two ingredients, endless refreshment.",
        "ingredients": [
            ("Gin", "2 oz", False), ("Tonic Water", "4 oz", False), ("Lime Wedge", "1", True),
        ],
        "instructions": [
            "Fill a highball glass with ice.",
            "Add gin, then top with tonic water.",
            "Squeeze in a lime wedge and stir once.",
        ],
    },
    {
        "slug": "cuba-libre", "name": "Cuba Libre", "kind": "cocktail", "icon": "🥤",
        "glass": "Highball", "image": "/images/Cuba-Libre-img.png",
        "description": "Rum and cola with a squeeze of lime that changes everything.",
        "ingredients": [
            ("Rum", "2 oz", False), ("Cola", "4 oz", False),
            ("Lime Juice", "½ oz", False), ("Lime Wedge", "1", True),
        ],
        "instructions": [
            "Fill a highball glass with ice.",
            "Add rum and lime juice, then top with cola.",
            "Garnish with a lime wedge.",
        ],
    },
    {
        "slug": "manhattan", "name": "Manhattan", "kind": "cocktail", "icon": "🍒",
        "glass": "Coupe", "image": "/images/Manhattan-img.png",
        "description": "Whiskey and sweet vermouth, stirred and elegant.",
        "ingredients": [
            ("Whiskey", "2 oz", False), ("Sweet Vermouth", "1 oz", False),
            ("Angostura Bitters", "2 dashes", False), ("Cocktail Cherry", "1", True),
        ],
        "instructions": [
            "Stir whiskey, sweet vermouth and bitters with ice.",
            "Strain into a chilled coupe.",
            "Garnish with a cherry.",
        ],
    },
    {
        "slug": "white-russian", "name": "White Russian", "kind": "cocktail", "icon": "🥛",
        "glass": "Rocks", "image": "/images/White-Russian-img.png",
        "description": "Vodka, coffee liqueur and cream. The Dude abides.",
        "ingredients": [
            ("Vodka", "2 oz", False), ("Coffee Liqueur", "1 oz", False),
            ("Heavy Cream", "1 oz", False),
        ],
        "instructions": [
            "Fill a rocks glass with ice.",
            "Add vodka and coffee liqueur.",
            "Float the heavy cream on top and stir gently.",
        ],
    },
    {
        "slug": "gimlet", "name": "Gimlet", "kind": "cocktail", "icon": "🍸",
        "glass": "Coupe", "image": "/images/Gimlet-img.png",
        "description": "Gin and lime, sharp and refreshing.",
        "ingredients": [
            ("Gin", "2 oz", False), ("Lime Juice", "¾ oz", False),
            ("Simple Syrup", "¾ oz", False), ("Lime Wedge", "1", True),
        ],
        "instructions": [
            "Shake gin, lime juice and simple syrup with ice.",
            "Strain into a chilled coupe.",
            "Garnish with a lime wedge.",
        ],
    },
    {
        "slug": "screwdriver", "name": "Screwdriver", "kind": "cocktail", "icon": "🍊",
        "glass": "Highball", "image": "/images/Screwdriver-img.png",
        "description": "Vodka and orange juice. Brunch approved.",
        "ingredients": [
            ("Vodka", "2 oz", False), ("Orange Juice", "4 oz", False),
            ("Orange Slice", "1", True),
        ],
        "instructions": [
            "Fill a highball glass with ice.",
            "Add vodka and top with orange juice.",
            "Stir and garnish with an orange slice.",
        ],
    },
    {
        "slug": "tequila-sunrise", "name": "Tequila Sunrise", "kind": "cocktail", "icon": "🌅",
        "glass": "Highball", "image": "/images/Tequila-Sunrise-img.png",
        "description": "Orange juice and tequila with a grenadine sunrise.",
        "ingredients": [
            ("Tequila", "2 oz", False), ("Orange Juice", "4 oz", False),
            ("Grenadine", "½ oz", False), ("Cocktail Cherry", "1", True),
        ],
        "instructions": [
            "Fill a highball glass with ice.",
            "Add tequila and orange juice and stir.",
            "Slowly pour grenadine down the side so it sinks to the bottom.",
            "Garnish with a cherry. Don't stir!",
        ],
    },
    {
        "slug": "kamikaze", "name": "Kamikaze", "kind": "shot", "icon": "🥂",
        "glass": "Shot glasses (makes 2)", "image": "/images/Kamikaze-img.png",
        "description": "Vodka, triple sec and lime — a crowd-pleasing shot.",
        "ingredients": [
            ("Vodka", "1 oz", False), ("Triple Sec", "1 oz", False), ("Lime Juice", "1 oz", False),
        ],
        "instructions": [
            "Shake all ingredients with ice.",
            "Strain into two shot glasses.",
        ],
    },
    {
        "slug": "lemon-drop-shot", "name": "Lemon Drop Shot", "kind": "shot", "icon": "🍋",
        "glass": "Shot glasses (makes 2)", "image": "/images/Lemon-Drop-Shot-img.png",
        "description": "Sweet-tart and dangerously easy to drink.",
        "ingredients": [
            ("Vodka", "1½ oz", False), ("Lemon Juice", "¾ oz", False),
            ("Simple Syrup", "½ oz", False),
            ("Sugar", "for the rim", True),
        ],
        "instructions": [
            "Optional: rim the shot glasses with sugar.",
            "Shake all ingredients with ice.",
            "Strain into two shot glasses.",
        ],
    },
    {
        "slug": "tequila-shot", "name": "Tequila Shot", "kind": "shot", "icon": "🧂",
        "glass": "Shot glass", "image": "/images/Tequila-Shot-img.png",
        "description": "Lick, shoot, suck. The classic ritual.",
        "ingredients": [
            ("Tequila", "1½ oz", False), ("Salt", "pinch", True), ("Lime Wedge", "1", True),
        ],
        "instructions": [
            "Pour tequila into a shot glass.",
            "Lick a pinch of salt from your hand.",
            "Take the shot, then bite the lime wedge.",
        ],
    },
    {
        "slug": "aperol-spritz", "name": "Aperol Spritz", "kind": "cocktail", "icon": "🥂",
        "glass": "Wine glass", "image": "/images/Aperol-Spritz-img.png",
        "description": "Bittersweet, bubbly and bright orange. Italy's favorite aperitivo.",
        "ingredients": [
            ("Prosecco", "3 oz", False), ("Aperol", "2 oz", False),
            ("Club Soda", "1 oz", False), ("Orange Slice", "1", True),
        ],
        "instructions": [
            "Fill a wine glass with ice.",
            "Add prosecco, then Aperol, then a splash of club soda.",
            "Stir gently once and garnish with an orange slice.",
        ],
    },
    {
        "slug": "french-75", "name": "French 75", "kind": "cocktail", "icon": "🥂",
        "glass": "Champagne flute", "image": "/images/French-75-img.png",
        "description": "Gin, lemon and bubbles. Celebratory and dangerously smooth.",
        "ingredients": [
            ("Gin", "1 oz", False), ("Lemon Juice", "½ oz", False),
            ("Simple Syrup", "½ oz", False), ("Prosecco", "3 oz", False),
            ("Lemon Twist", "1", True),
        ],
        "instructions": [
            "Shake gin, lemon juice and simple syrup with ice.",
            "Strain into a champagne flute.",
            "Top with prosecco (or Champagne) and garnish with a lemon twist.",
        ],
    },
    {
        "slug": "hugo-spritz", "name": "Hugo Spritz", "kind": "cocktail", "icon": "🌸",
        "glass": "Wine glass", "image": "/images/Hugo-Spritz-img.png",
        "description": "Elderflower, mint and prosecco. Light, floral and refreshing.",
        "ingredients": [
            ("Prosecco", "3 oz", False), ("Elderflower Liqueur", "1 oz", False),
            ("Club Soda", "1 oz", False), ("Mint", "4–5 leaves", False),
            ("Lime Wedge", "1", True),
        ],
        "instructions": [
            "Clap the mint leaves between your hands and drop them in a wine glass.",
            "Add elderflower liqueur and fill the glass with ice.",
            "Top with prosecco and club soda, then stir gently.",
            "Garnish with a lime wedge.",
        ],
    },
    {
        "slug": "pina-colada", "name": "Piña Colada", "kind": "cocktail", "icon": "🍍",
        "glass": "Hurricane", "image": "/images/Pina-Colada-img.png",
        "description": "Creamy coconut and pineapple. A vacation you can blend.",
        "ingredients": [
            ("Rum", "2 oz", False), ("Coconut Cream", "1½ oz", False),
            ("Pineapple Juice", "3 oz", False), ("Pineapple Wedge", "1", True),
            ("Cocktail Cherry", "1", True),
        ],
        "instructions": [
            "Add rum, coconut cream and pineapple juice to a blender with 1 cup of ice.",
            "Blend until smooth.",
            "Pour into a hurricane glass.",
            "Garnish with a pineapple wedge and a cherry.",
        ],
    },
    {
        "slug": "blue-hawaiian", "name": "Blue Hawaiian", "kind": "cocktail", "icon": "🌊",
        "glass": "Hurricane", "image": "/images/Blue-Hawaiian-img.png",
        "description": "Tropical, creamy and electric blue.",
        "ingredients": [
            ("Rum", "1½ oz", False), ("Blue Curaçao", "¾ oz", False),
            ("Pineapple Juice", "3 oz", False), ("Coconut Cream", "¾ oz", False),
            ("Pineapple Wedge", "1", True), ("Cocktail Cherry", "1", True),
        ],
        "instructions": [
            "Shake all ingredients hard with ice (or blend with 1 cup of ice).",
            "Pour into a hurricane glass filled with ice.",
            "Garnish with a pineapple wedge and a cherry.",
        ],
    },
    {
        "slug": "bloody-mary", "name": "Bloody Mary", "kind": "cocktail", "icon": "🍅",
        "glass": "Highball", "image": "/images/Bloody-Mary-img.png",
        "description": "Savory, spicy and the undisputed king of brunch.",
        "ingredients": [
            ("Vodka", "2 oz", False), ("Tomato Juice", "4 oz", False),
            ("Lemon Juice", "½ oz", False), ("Worcestershire Sauce", "2 dashes", False),
            ("Hot Sauce", "2 dashes", False), ("Salt", "pinch", True),
            ("Celery Stalk", "1", True), ("Lemon Wedge", "1", True),
        ],
        "instructions": [
            "Fill a highball glass with ice.",
            "Add vodka, tomato juice, lemon juice, Worcestershire and hot sauce.",
            "Season with a pinch of salt and roll it back and forth with another glass to mix.",
            "Garnish with a celery stalk and a lemon wedge.",
        ],
    },
    {
        "slug": "spicy-margarita", "name": "Spicy Margarita", "kind": "cocktail", "icon": "🌶️",
        "glass": "Rocks", "image": "/images/Spicy-Margarita-img.png",
        "description": "The classic margarita with a jalapeño kick.",
        "ingredients": [
            ("Tequila", "2 oz", False), ("Lime Juice", "1 oz", False),
            ("Triple Sec", "½ oz", False), ("Agave Syrup", "½ oz", False),
            ("Jalapeño", "2–3 slices", False), ("Salt", "for the rim", True),
        ],
        "instructions": [
            "Optional: salt the rim of a rocks glass.",
            "Muddle jalapeño slices in a shaker.",
            "Add tequila, lime juice, triple sec, agave and ice, then shake well.",
            "Strain into the glass over fresh ice and garnish with a jalapeño slice.",
        ],
    },
    {
        "slug": "oaxaca-old-fashioned", "name": "Oaxaca Old Fashioned", "kind": "cocktail",
        "icon": "🔥", "glass": "Rocks", "image": "/images/Oaxaca-Old-Fashioned-img.png",
        "description": "A smoky agave spin on the Old Fashioned.",
        "ingredients": [
            ("Tequila", "1½ oz", False), ("Mezcal", "½ oz", False),
            ("Agave Syrup", "1 tsp", False), ("Angostura Bitters", "2 dashes", False),
            ("Orange Peel", "1 twist", True),
        ],
        "instructions": [
            "Stir tequila, mezcal, agave syrup and bitters with ice.",
            "Strain into a rocks glass over one large ice cube.",
            "Express an orange peel over the drink and drop it in.",
        ],
    },
    {
        "slug": "ranch-water", "name": "Ranch Water", "kind": "cocktail", "icon": "🌵",
        "glass": "Highball", "image": "/images/Ranch-Water-img.png",
        "description": "Tequila, lime and bubbles. West Texas simple.",
        "ingredients": [
            ("Tequila", "2 oz", False), ("Lime Juice", "1 oz", False),
            ("Club Soda", "4 oz", False), ("Lime Wedge", "1", True),
        ],
        "instructions": [
            "Fill a highball glass with ice.",
            "Add tequila and lime juice.",
            "Top with club soda (or sparkling mineral water) and garnish with a lime wedge.",
        ],
    },
    {
        "slug": "mint-julep", "name": "Mint Julep", "kind": "cocktail", "icon": "🌿",
        "glass": "Julep cup", "image": "/images/Mint-Julep-img.png",
        "description": "Bourbon, mint and a mountain of crushed ice. Derby Day classic.",
        "ingredients": [
            ("Bourbon", "2½ oz", False), ("Simple Syrup", "½ oz", False),
            ("Mint", "8 leaves", False),
        ],
        "instructions": [
            "Gently muddle mint leaves with simple syrup in a julep cup.",
            "Add bourbon and pack the cup with crushed ice.",
            "Stir until the cup frosts, then top with more crushed ice.",
            "Garnish with a big mint sprig.",
        ],
    },
    {
        "slug": "boulevardier", "name": "Boulevardier", "kind": "cocktail", "icon": "🥃",
        "glass": "Rocks", "image": "/images/Boulevardier-img.png",
        "description": "A Negroni made with bourbon. Richer, warmer, just as bold.",
        "ingredients": [
            ("Bourbon", "1¼ oz", False), ("Campari", "1 oz", False),
            ("Sweet Vermouth", "1 oz", False), ("Orange Peel", "1 twist", True),
        ],
        "instructions": [
            "Stir bourbon, Campari and sweet vermouth with ice.",
            "Strain into a rocks glass over a large ice cube.",
            "Garnish with an orange peel.",
        ],
    },
    {
        "slug": "gold-rush", "name": "Gold Rush", "kind": "cocktail", "icon": "🍯",
        "glass": "Rocks", "image": "/images/Gold-Rush-img.png",
        "description": "Bourbon, honey and lemon. A whiskey sour's golden cousin.",
        "ingredients": [
            ("Bourbon", "2 oz", False), ("Lemon Juice", "¾ oz", False),
            ("Honey Syrup", "¾ oz", False), ("Lemon Twist", "1", True),
        ],
        "instructions": [
            "Shake bourbon, lemon juice and honey syrup with ice.",
            "Strain into a rocks glass over a large ice cube.",
            "Garnish with a lemon twist.",
        ],
    },
    {
        "slug": "rob-roy", "name": "Rob Roy", "kind": "cocktail", "icon": "🍒",
        "glass": "Coupe", "image": "/images/Rob-Roy-img.png",
        "description": "A Manhattan made with Scotch. Smooth with a hint of smoke.",
        "ingredients": [
            ("Scotch", "2 oz", False), ("Sweet Vermouth", "1 oz", False),
            ("Angostura Bitters", "2 dashes", False), ("Cocktail Cherry", "1", True),
        ],
        "instructions": [
            "Stir Scotch, sweet vermouth and bitters with ice.",
            "Strain into a chilled coupe.",
            "Garnish with a cherry.",
        ],
    },
    {
        "slug": "sidecar", "name": "Sidecar", "kind": "cocktail", "icon": "🍋",
        "glass": "Coupe", "image": "/images/Sidecar-img.png",
        "description": "Cognac, orange and lemon with a sugared rim.",
        "ingredients": [
            ("Cognac", "1½ oz", False), ("Triple Sec", "¾ oz", False),
            ("Lemon Juice", "¾ oz", False), ("Sugar", "for the rim", True),
            ("Orange Peel", "1 twist", True),
        ],
        "instructions": [
            "Optional: rim a coupe with sugar.",
            "Shake cognac, triple sec and lemon juice with ice.",
            "Strain into the coupe and garnish with an orange twist.",
        ],
    },
    {
        "slug": "brandy-alexander", "name": "Brandy Alexander", "kind": "cocktail", "icon": "🍫",
        "glass": "Coupe", "image": "/images/Brandy-Alexander-img.png",
        "description": "Brandy, chocolate and cream. Dessert in a coupe.",
        "ingredients": [
            ("Brandy", "1½ oz", False), ("Chocolate Liqueur", "1 oz", False),
            ("Heavy Cream", "1 oz", False), ("Nutmeg", "pinch", True),
        ],
        "instructions": [
            "Shake brandy, chocolate liqueur and cream hard with ice.",
            "Strain into a chilled coupe.",
            "Dust with freshly grated nutmeg.",
        ],
    },
    {
        "slug": "bees-knees", "name": "Bee's Knees", "kind": "cocktail", "icon": "🐝",
        "glass": "Coupe", "image": "/images/Bees-Knees-img.png",
        "description": "A Prohibition-era sour sweetened with honey.",
        "ingredients": [
            ("Gin", "2 oz", False), ("Lemon Juice", "¾ oz", False),
            ("Honey Syrup", "¾ oz", False), ("Lemon Twist", "1", True),
        ],
        "instructions": [
            "Shake gin, lemon juice and honey syrup with ice.",
            "Strain into a chilled coupe.",
            "Garnish with a lemon twist.",
        ],
    },
    {
        "slug": "clover-club", "name": "Clover Club", "kind": "cocktail", "icon": "🍓",
        "glass": "Coupe", "image": "/images/Clover-Club-img.png",
        "description": "Gin and raspberry with a silky foam top.",
        "ingredients": [
            ("Gin", "1½ oz", False), ("Raspberry Liqueur", "½ oz", False),
            ("Lemon Juice", "½ oz", False), ("Simple Syrup", "¼ oz", False),
            ("Egg White", "1", False),
        ],
        "instructions": [
            "Shake all ingredients without ice for 15 seconds (a dry shake) to build foam.",
            "Add ice and shake again until well chilled.",
            "Strain into a chilled coupe.",
        ],
    },
    {
        "slug": "gin-basil-smash", "name": "Gin Basil Smash", "kind": "cocktail", "icon": "🌿",
        "glass": "Rocks", "image": "/images/Gin-Basil-Smash-img.png",
        "description": "Bright green, herbal and zesty. A modern classic.",
        "ingredients": [
            ("Gin", "2 oz", False), ("Lemon Juice", "¾ oz", False),
            ("Simple Syrup", "½ oz", False), ("Basil", "8–10 leaves", False),
        ],
        "instructions": [
            "Muddle basil with lemon juice and simple syrup in a shaker.",
            "Add gin and ice and shake hard.",
            "Double strain into a rocks glass over fresh ice.",
            "Garnish with a basil sprig.",
        ],
    },
    {
        "slug": "strawberry-daiquiri", "name": "Strawberry Daiquiri", "kind": "cocktail",
        "icon": "🍓", "glass": "Coupe", "image": "/images/Strawberry-Daiquiri-img.png",
        "description": "The classic daiquiri with fresh muddled strawberries.",
        "ingredients": [
            ("Rum", "2 oz", False), ("Lime Juice", "1 oz", False),
            ("Simple Syrup", "¾ oz", False), ("Strawberries", "3–4", False),
        ],
        "instructions": [
            "Muddle strawberries with simple syrup in a shaker.",
            "Add rum, lime juice and ice and shake well.",
            "Double strain into a chilled coupe and garnish with a strawberry.",
        ],
    },
    {
        "slug": "blueberry-mojito", "name": "Blueberry Mojito", "kind": "cocktail", "icon": "🫐",
        "glass": "Highball", "image": "/images/Blueberry-Mojito-img.png",
        "description": "Everything you love about a mojito, plus juicy blueberries.",
        "ingredients": [
            ("Rum", "2 oz", False), ("Lime Juice", "¾ oz", False),
            ("Simple Syrup", "½ oz", False), ("Mint", "6–8 leaves", False),
            ("Blueberries", "10–12", False), ("Club Soda", "top", False),
        ],
        "instructions": [
            "Gently muddle blueberries and mint with lime juice and simple syrup.",
            "Add rum and fill the glass with ice.",
            "Top with club soda and stir.",
            "Garnish with a mint sprig and a few blueberries.",
        ],
    },
    {
        "slug": "greyhound", "name": "Greyhound", "kind": "cocktail", "icon": "🐕",
        "glass": "Highball", "image": "/images/Greyhound-img.png",
        "description": "Vodka and fresh grapefruit. Salt the rim and it's a Salty Dog.",
        "ingredients": [
            ("Vodka", "2 oz", False), ("Grapefruit Juice", "4 oz", False),
            ("Salt", "for the rim", True), ("Rosemary", "1 sprig", True),
        ],
        "instructions": [
            "Optional: salt the rim of a highball glass for a Salty Dog.",
            "Fill the glass with ice and add vodka.",
            "Top with grapefruit juice and stir.",
            "Garnish with a rosemary sprig.",
        ],
    },
    {
        "slug": "fuzzy-navel", "name": "Fuzzy Navel", "kind": "cocktail", "icon": "🍑",
        "glass": "Highball", "image": "/images/Fuzzy-Navel-img.png",
        "description": "Peach schnapps and orange juice. Sweet, simple and retro.",
        "ingredients": [
            ("Peach Schnapps", "2 oz", False), ("Orange Juice", "4 oz", False),
            ("Orange Slice", "1", True),
        ],
        "instructions": [
            "Fill a highball glass with ice.",
            "Add peach schnapps and top with orange juice.",
            "Stir and garnish with an orange slice.",
        ],
    },
    {
        "slug": "mudslide", "name": "Mudslide", "kind": "cocktail", "icon": "🍦",
        "glass": "Rocks", "image": "/images/Mudslide-img.png",
        "description": "Vodka, coffee liqueur and Irish cream. A boozy milkshake.",
        "ingredients": [
            ("Vodka", "1 oz", False), ("Coffee Liqueur", "1 oz", False),
            ("Irish Cream", "1 oz", False), ("Heavy Cream", "1 oz", False),
        ],
        "instructions": [
            "Shake all ingredients with ice.",
            "Strain into a rocks glass over fresh ice.",
            "Optional: drizzle chocolate syrup inside the glass first.",
        ],
    },
    {
        "slug": "chocolate-martini", "name": "Chocolate Martini", "kind": "cocktail", "icon": "🍫",
        "glass": "Martini", "image": "/images/Chocolate-Martini-img.png",
        "description": "Silky, chocolatey and perfect after dinner.",
        "ingredients": [
            ("Vodka", "1½ oz", False), ("Chocolate Liqueur", "1 oz", False),
            ("Irish Cream", "1 oz", False), ("Chocolate Bitters", "1 dash", True),
        ],
        "instructions": [
            "Shake vodka, chocolate liqueur, Irish cream and bitters with ice.",
            "Strain into a chilled martini glass.",
            "Optional: rim the glass with cocoa powder.",
        ],
    },
    {
        "slug": "strawberries-and-cream", "name": "Strawberries & Cream", "kind": "cocktail",
        "icon": "🍓", "glass": "Rocks", "image": "/images/Strawberries-Cream-img.png",
        "description": "Pink, creamy and sweet. Like a strawberry milkshake.",
        "ingredients": [
            ("Strawberry Cream Liqueur", "2 oz", False), ("Vodka", "1 oz", False),
            ("Milk", "2 oz", False), ("Strawberries", "1–2", True),
        ],
        "instructions": [
            "Shake strawberry cream liqueur, vodka and milk with ice.",
            "Strain into a rocks glass over fresh ice.",
            "Garnish with a sliced strawberry on the rim.",
        ],
    },
    {
        "slug": "b-52", "name": "B-52", "kind": "shot", "icon": "🎯",
        "glass": "Shot glass", "image": "/images/B-52-img.png",
        "description": "Three perfect layers: coffee, cream and orange.",
        "ingredients": [
            ("Coffee Liqueur", "½ oz", False), ("Irish Cream", "½ oz", False),
            ("Triple Sec", "½ oz", False),
        ],
        "instructions": [
            "Pour coffee liqueur into a shot glass.",
            "Slowly pour Irish cream over the back of a spoon so it floats on top.",
            "Float triple sec on top the same way.",
        ],
    },
    {
        "slug": "baby-guinness", "name": "Baby Guinness", "kind": "shot", "icon": "🍺",
        "glass": "Shot glass", "image": "/images/Baby-Guinness-img.png",
        "description": "A shot that looks like a tiny pint of stout.",
        "ingredients": [
            ("Coffee Liqueur", "1¼ oz", False), ("Irish Cream", "¼ oz", False),
        ],
        "instructions": [
            "Pour coffee liqueur into a shot glass, leaving room at the top.",
            "Slowly pour Irish cream over the back of a spoon to make the 'head'.",
        ],
    },
    {
        "slug": "chocolate-covered-strawberry-espresso-martini",
        "name": "Chocolate Covered Strawberry Espresso Martini", "kind": "cocktail", "icon": "🍓",
        "glass": "Martini", "image": "/images/Choc-Strawberry-Espresso-Martini-img.png",
        "description": "Strawberry cream, chocolate and espresso. Drew's house favorite.",
        "ingredients": [
            ("Vodka", "1 oz", False), ("Strawberry Cream Liqueur", "1 oz", False),
            ("Espresso", "1 oz", False), ("Chocolate Liqueur", "½ oz", False),
            ("Strawberries", "1", True),
        ],
        "instructions": [
            "Add vodka, strawberry cream liqueur, espresso and chocolate liqueur to a shaker with ice.",
            "Shake hard until frothy.",
            "Strain into a chilled martini glass.",
            "Garnish with a strawberry on the rim (dip it in melted chocolate first if you like).",
        ],
    },
]
