"""Reset the database and load the catalog from seed_data.py.

Usage (from the server/ folder):
    python seed.py

The app also does this automatically on startup whenever seed_data.py has changed
(see catalog_fingerprint), so deploys pick up new drinks without a manual seed.
"""
import hashlib
import json

import seed_data
from seed_data import DRINKS, FLAVORS, INGREDIENTS, STRENGTHS, VIBES


def catalog_fingerprint():
    """A short hash of the whole catalog. It changes whenever seed_data.py's data changes."""
    payload = json.dumps(
        {"ingredients": INGREDIENTS, "drinks": DRINKS, "flavors": FLAVORS,
         "strengths": STRENGTHS, "vibes": VIBES},
        sort_keys=True, ensure_ascii=False, default=list,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def validate_catalog():
    """Catch typos in seed_data.py before anything touches the database."""
    known = {n for names in INGREDIENTS.values() for n in names}
    problems = []
    for d in DRINKS:
        name = d.get("name", d.get("slug"))
        for ing, _, _ in d["ingredients"]:
            if ing not in known:
                problems.append(f"{name}: unknown ingredient '{ing}'")
        flavors = d.get("flavors", [])
        if not flavors:
            problems.append(f"{name}: needs at least one flavor")
        problems += [f"{name}: unknown flavor '{f}'" for f in flavors if f not in FLAVORS]
        if d.get("strength") not in STRENGTHS:
            problems.append(f"{name}: strength must be one of {STRENGTHS}")
        vibes = d.get("vibes", [])
        if not vibes:
            problems.append(f"{name}: needs at least one vibe")
        problems += [f"{name}: unknown vibe '{v}'" for v in vibes if v not in VIBES]
    if problems:
        raise ValueError("seed_data.py has problems:\n  " + "\n  ".join(problems))


def seed_database(db, reset=True):
    """Optionally drop tables, recreate them, and insert the catalog."""
    validate_catalog()
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
            """INSERT INTO drinks (slug, name, description, kind, glass, icon, image_url, strength)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id""",
            (d["slug"], d["name"], d["description"], d["kind"], d["glass"], d["icon"],
             d["image"], d["strength"]),
        )
        drink_id = row["id"]
        for pos, (name, amount, optional) in enumerate(d["ingredients"]):
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
        for tag_type, tags in (("flavor", d["flavors"]), ("vibe", d["vibes"])):
            for pos, tag in enumerate(tags):
                db.execute(
                    "INSERT INTO drink_tags (drink_id, tag_type, tag, position) VALUES (%s, %s, %s, %s)",
                    (drink_id, tag_type, tag, pos),
                )

    db.execute("DELETE FROM catalog_meta WHERE key = %s", ("fingerprint",))
    db.execute("INSERT INTO catalog_meta (key, value) VALUES (%s, %s)",
               ("fingerprint", catalog_fingerprint()))
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
