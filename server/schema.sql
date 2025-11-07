-- Create database
CREATE DATABASE IF NOT EXISTS nook_pour;
USE nook_pour;

-- Drinks table
CREATE TABLE IF NOT EXISTS drinks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    instructions TEXT,
    image_url VARCHAR(255)
);

-- Ingredients table
CREATE TABLE IF NOT EXISTS ingredients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- Join table for many-to-many relationship
CREATE TABLE IF NOT EXISTS drink_ingredients (
    drink_id INT,
    ingredient_id INT,
    measure VARCHAR(50),
    PRIMARY KEY (drink_id, ingredient_id),
    FOREIGN KEY (drink_id) REFERENCES drinks(id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(id) ON DELETE CASCADE
);

-- Optional sample data
INSERT INTO drinks (name, category, instructions, image_url)
VALUES
('Margarita', 'Cocktail', 'Shake all ingredients with ice and strain into a glass.', 'https://example.com/margarita.jpg'),
('Old Fashioned', 'Cocktail', 'Stir ingredients with ice and strain into a glass.', 'https://example.com/oldfashioned.jpg');

INSERT INTO ingredients (name)
VALUES ('Tequila'), ('Triple Sec'), ('Lime Juice'), ('Whiskey'), ('Bitters'), ('Simple Syrup');

INSERT INTO drink_ingredients (drink_id, ingredient_id, measure)
VALUES
(1, 1, '2 oz'),
(1, 2, '1 oz'),
(1, 3, '1 oz'),
(2, 4, '2 oz'),
(2, 5, '2 dashes'),
(2, 6, '1 tsp');
