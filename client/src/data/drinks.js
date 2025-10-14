export const SAMPLE_INGREDIENTS = [
    "Vodka",
    "Gin",
    "Rum",
    "Tequila",
    "Whiskey",
    "Triple Sec",
    "Dry Vermouth",
    "Lime Juice",
    "Lemon Juice",
    "Simple Syrup",
    "Angostura Bitters",
    "Club Soda",
    "Coffee Liqueur",
    "Espresso",
];


export const SAMPLE_DRINKS = [
    {
        id: "margarita",
        name: "Margarita",
        icon: "🥃",
        ingredients: ["Tequila", "Triple Sec", "Lime Juice"],
        instructions: [
            "Combine ingredients in a shaker with ice.",
            "Shake well and strain into a chilled glass.",
            "Garnish with a lime wedge.",
        ],
    },
    {
        id: "martini",
        name: "Martini",
        icon: "🍸",
        ingredients: ["Gin", "Dry Vermouth"],
        instructions: [
            "Stir with ice and strain into a chilled martini glass.", 
            "Garnish with an olive."
        ],
    },
    {
        id: "mojito",
        name: "Mojito",
        icon: "🍹",
        ingredients: ["Rum", "Lime Juice", "Simple Syrup", "Club Soda"],
        instructions: [
            "Muddle mint and lime with simple syrup.",
            "Add rum and ice, top with club soda.",
            "Garnish with a mint sprig.",
        ],
    },
    {
        id: "whiskey_sour",
        name: "Whiskey Sour",
        icon: "🥃",
        ingredients: ["Whiskey", "Lemon Juice", "Simple Syrup"],
        instructions: ["Shake with ice and strain into a rocks glass.", "Garnish with a cherry."],
    },
    {
        id: "old_fashion",
        name: "Old Fashion",
        icon: "🥃",
        ingredients: ["Whiskey", "Angostura Bitters", "Simple Syrup"],
        instructions: [
            "Add whiskey, bitters, and simple syrup into a mixing glass with ice.",
            "Stir until well-chilled.",
            "Strain into a rocks glass over one large ice cube.",
            "Optional: Garnish with an orange peel twist.",
        ],
    },
    {
        id: "espresso_martini",
        name: "Espresso Martini",
        icon: "☕",
        ingredients: ["Vodka", "Coffee Liqueur", "Espresso", "Simple Syrup"],
        instructions: [
        "Shake all ingredients with ice until frothy.",
        "Strain into a chilled martini glass.",
        "Garnish with coffee beans.",
        ],
    },
];