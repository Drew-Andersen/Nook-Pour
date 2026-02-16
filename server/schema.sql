-- Create the Database
CREATE DATABASE IF NOT EXISTS nook_pour;
USE nook_pour;

-- Development Reset
DROP TABLE IF EXISTS drink_ingredients;
DROP TABLE IF EXISTS drinks;
DROP TABLE IF EXISTS ingredients;

-- Ingredients Table
CREATE TABLE ingredients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    category ENUM('alcohol', 'mixer', 'garnish') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Drinks Table
CREATE TABLE drinks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL UNIQUE,
    description TEXT,
    instructions TEXT NOT NULL,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Join Table 
CREATE TABLE drink_ingredients (
    drink_name VARCHAR(150) NOT NULL,
    ingredient_name VARCHAR(150) NOT NULL,
    quantity VARCHAR(100), 

    PRIMARY KEY (drink_name, ingredient_name),

    FOREIGN KEY (drink_name)
        REFERENCES drinks(name)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (ingredient_name)
        REFERENCES ingredients(name)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
