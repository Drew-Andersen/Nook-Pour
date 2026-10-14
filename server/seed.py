"""Reset the database and load the starter catalog from seed_data.py.

Usage (from the server/ folder):
    python seed.py
"""
from seed_data import DRINKS, INGREDIENTS


def seed_database(db, reset=True):
    """Optionally drop tables, recreate them, and insert the starter catalog."""
    if reset:
        db.drop_schema()
    db.create_schema()

    ids = {}
    for category, names in INGREDIENTS.items():
        for name in names:
            row = db.one(
                "INSERT INTO ingredients (name, category) VALUES (%s, %s) RETURNING id",
                (name, category),
            )
            ids[name] = row["id"]

    for d in DRINKS:
        row = db.one(
            """INSERT INTO drinks (slug, name, description, kind, glass, icon, image_url)
               VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id""",
            (d["slug"], d["name"], d["description"], d["kind"], d["glass"], d["icon"], d["image"]),
        )
        drink_id = row["id"]
        for pos, (name, amount, optional) in enumerate(d["ingredients"]):
            if name not in ids:
                db.rollback()
                raise ValueError(f"{d['name']} uses unknown ingredient '{name}'")
            db.execute(
                """INSERT INTO drink_ingredients (drink_id, ingredient_id, amount, optional, position)
                   VALUES (%s, %s, %s, %s, %s)""",
                (drink_id, ids[name], amount, optional, pos),
            )
        for pos, step in enumerate(d["instructions"]):
            db.execute(
                "INSERT INTO drink_steps (drink_id, position, step) VALUES (%s, %s, %s)",
                (drink_id, pos, step),
            )

    db.commit()
    return len(ids), len(DRINKS)


if __name__ == "__main__":
    from dotenv import load_dotenv

    from db import Database, database_url

    load_dotenv()
    database = Database(database_url())
    n_ing, n_drinks = seed_database(database)
    database.close()
    print(f"Seeded {n_ing} ingredients and {n_drinks} drinks.")
