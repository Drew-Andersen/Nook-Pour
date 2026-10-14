"""Queries and business logic for drinks and ingredients."""
from collections import defaultdict

# Category keys -> display labels (also the display order on the client).
INGREDIENT_CATEGORIES = {
    "spirit": "Spirits",
    "liqueur": "Liqueurs & Vermouths",
    "mixer": "Mixers & Juices",
    "garnish": "Garnishes",
}


def list_ingredients(db):
    rows = db.query("SELECT id, name, category FROM ingredients ORDER BY name")
    order = list(INGREDIENT_CATEGORIES)
    rows.sort(key=lambda r: (order.index(r["category"]) if r["category"] in order else 99, r["name"]))
    return rows


def load_drinks(db, search=None, kind=None, slug=None):
    """Return fully assembled drinks (ingredients + steps), sorted by name."""
    where, params = [], []
    if slug:
        where.append("d.slug = %s")
        params.append(slug)
    if kind:
        where.append("d.kind = %s")
        params.append(kind)
    if search:
        like = f"%{search.lower()}%"
        where.append(
            """(LOWER(d.name) LIKE %s OR d.id IN (
                   SELECT di.drink_id FROM drink_ingredients di
                   JOIN ingredients i ON i.id = di.ingredient_id
                   WHERE LOWER(i.name) LIKE %s))"""
        )
        params += [like, like]
    sql = "SELECT d.* FROM drinks d"
    if where:
        sql += " WHERE " + " AND ".join(where)
    drinks = db.query(sql + " ORDER BY d.name", params)
    if not drinks:
        return []

    ids = [d["id"] for d in drinks]
    marks = ", ".join(["%s"] * len(ids))
    components = db.query(
        f"""SELECT di.drink_id, i.name, i.category, di.amount, di.optional
            FROM drink_ingredients di JOIN ingredients i ON i.id = di.ingredient_id
            WHERE di.drink_id IN ({marks}) ORDER BY di.drink_id, di.position""",
        ids,
    )
    steps = db.query(
        f"""SELECT drink_id, step FROM drink_steps
            WHERE drink_id IN ({marks}) ORDER BY drink_id, position""",
        ids,
    )
    by_drink = defaultdict(list)
    for c in components:
        by_drink[c["drink_id"]].append(
            {
                "name": c["name"],
                "category": c["category"],
                "amount": c["amount"],
                "optional": bool(c["optional"]),
            }
        )
    steps_by_drink = defaultdict(list)
    for s in steps:
        steps_by_drink[s["drink_id"]].append(s["step"])

    return [
        {
            "id": d["slug"],
            "name": d["name"],
            "description": d["description"],
            "kind": d["kind"],
            "glass": d["glass"],
            "icon": d["icon"],
            "image": d["image_url"],
            "ingredients": by_drink[d["id"]],
            "instructions": steps_by_drink[d["id"]],
        }
        for d in drinks
    ]


def match_drinks(drinks, have_names, max_missing=2):
    """Split drinks into ones you can make now and ones you're close to.

    Optional ingredients (garnishes, rims) never block a match.
    """
    have = {n.strip().lower() for n in have_names if isinstance(n, str) and n.strip()}
    can_make, almost = [], []
    unlocks = defaultdict(list)  # ingredient -> drinks it would complete

    for drink in drinks:
        required = [i["name"] for i in drink["ingredients"] if not i["optional"]]
        missing = sorted(n for n in required if n.lower() not in have)
        if not missing:
            can_make.append(drink)
        elif len(missing) <= max_missing and len(missing) < len(required):
            almost.append({**drink, "missing": missing})
            if len(missing) == 1:
                unlocks[missing[0]].append(drink["name"])

    almost.sort(key=lambda d: (len(d["missing"]), d["name"]))
    top_unlocks = sorted(
        ({"ingredient": k, "count": len(v), "drinks": v} for k, v in unlocks.items()),
        key=lambda u: (-u["count"], u["ingredient"]),
    )[:5]
    return {"can_make": can_make, "almost": almost, "unlocks": top_unlocks}
