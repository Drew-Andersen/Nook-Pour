CREATE TABLE IF NOT EXISTS ingredients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    category VARCHAR(20) NOT NULL
        CHECK (category IN ('spirit', 'liqueur', 'mixer', 'garnish')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS drinks (
    id SERIAL PRIMARY KEY,
    slug VARCHAR(150) NOT NULL UNIQUE,
    name VARCHAR(150) NOT NULL UNIQUE,
    description TEXT,
    kind VARCHAR(20) NOT NULL DEFAULT 'cocktail' CHECK (kind IN ('cocktail', 'shot')),
    glass VARCHAR(60),
    icon VARCHAR(8),
    image_url TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Which ingredients go in which drink, and how much.
CREATE TABLE IF NOT EXISTS drink_ingredients (
    drink_id INTEGER NOT NULL REFERENCES drinks(id) ON DELETE CASCADE,
    ingredient_id INTEGER NOT NULL REFERENCES ingredients(id) ON DELETE CASCADE,
    amount VARCHAR(50),
    optional BOOLEAN NOT NULL DEFAULT FALSE,  -- garnishes/rims never block a match
    position INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (drink_id, ingredient_id)
);

-- Ordered recipe steps.
CREATE TABLE IF NOT EXISTS drink_steps (
    drink_id INTEGER NOT NULL REFERENCES drinks(id) ON DELETE CASCADE,
    position INTEGER NOT NULL,
    step TEXT NOT NULL,
    PRIMARY KEY (drink_id, position)
);

CREATE INDEX IF NOT EXISTS idx_drink_ingredients_ingredient
    ON drink_ingredients (ingredient_id);
