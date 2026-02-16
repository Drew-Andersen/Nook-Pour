USE nook_pour;

-- Inserting ingredents
INSERT INTO ingredients (name, category) VALUES
-- Alcohols
('Tequila', 'alcohol'),
('Vodka', 'alcohol'),
('Gin', 'alcohol'),
('Rum', 'alcohol'),
('Whiskey', 'alcohol'),
('Triple Sec', 'alcohol'),
('Dry Vermouth', 'alcohol'),
('Coffee Liqueur', 'alcohol'),

-- Mixers
('Lime Juice', 'mixer'),
('Lemon Juice', 'mixer'),
('Simple Syrup', 'mixer'),
('Angostura Bitters', 'mixer'),
('Club Soda', 'mixer'),
('Espresso', 'mixer'),
('Heavy Cream', 'mixer'),
('Pumpkin Puree', 'mixer'),

-- Garnishes
('Mint', 'garnish'),
('Salt Rim', 'garnish'),
('Lime Wedge', 'garnish');

-- Inserting drinks
INSERT INTO drinks (name, description, instructions, image_url) VALUES
(
    'Margarita',
    'A classic tequila-based cocktail with citrus flavor.',
    'Shake tequila, lime juice, and triple sec with ice. Strain into a salt-rimmed glass.',
    NULL
),
(
    'Mojito',
    'A refreshing Cuban highball.',
    'Muddle mint with lime juice and simple syrup. Add rum and top with club soda. Garnish with mint.',
    NULL
);

INSERT INTO drink_ingredients (drink_name, ingredient_name, quantity) VALUES
('Margarita', 'Tequila', '2 oz'),
('Margarita', 'Lime Juice', '1 oz'),
('Margarita', 'Triple Sec', '1 oz'),
('Margarita', 'Salt Rim', 'To taste'),
('Mojito', 'Rum', '2 oz'),
('Mojito', 'Lime Juice', '1 oz'),
('Mojito', 'Simple Syrup', '0.5 oz'),
('Mojito', 'Club Soda', 'Top off'),
('Mojito', 'Mint', '6 leaves');