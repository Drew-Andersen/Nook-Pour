"""API tests. Run from server/:  python -m pytest   (or: python -m unittest)

Uses an in-memory SQLite database, so no Postgres is needed to run them.
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import create_app  # noqa: E402
from db import Database  # noqa: E402
from seed_data import DRINKS, INGREDIENTS  # noqa: E402


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.db = Database("sqlite://")
        self.app = create_app(
            {"TESTING": True, "SHARED_DB": self.db, "CLIENT_DIST": "/nonexistent"}
        )
        self.client = self.app.test_client()

    def tearDown(self):
        self.db.close()

    def test_health_reports_seeded_drinks(self):
        res = self.client.get("/api/health")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["drinks"], len(DRINKS))

    def test_ingredients_grouped_by_category(self):
        data = self.client.get("/api/ingredients").get_json()
        self.assertEqual([c["key"] for c in data["categories"]], list(INGREDIENTS))
        names = [i["name"] for i in data["ingredients"]]
        self.assertEqual(len(names), sum(len(v) for v in INGREDIENTS.values()))
        self.assertEqual(data["ingredients"][0]["category"], "spirit")

    def test_list_and_search_drinks(self):
        all_drinks = self.client.get("/api/drinks").get_json()
        self.assertEqual(len(all_drinks), len(DRINKS))
        marg = next(d for d in all_drinks if d["id"] == "margarita")
        self.assertEqual(marg["ingredients"][0], {
            "name": "Tequila", "category": "spirit", "amount": "2 oz", "optional": False})
        self.assertTrue(marg["instructions"])

        by_ing = {d["name"] for d in self.client.get("/api/drinks?q=campari").get_json()}
        self.assertEqual(by_ing, {"Negroni", "Boulevardier"})
        by_name = {d["name"] for d in self.client.get("/api/drinks?q=MARG").get_json()}
        self.assertEqual(by_name, {"Margarita", "Spicy Margarita"})
        shots = self.client.get("/api/drinks?kind=shot").get_json()
        self.assertTrue(shots and all(d["kind"] == "shot" for d in shots))

    def test_get_one_drink_and_404(self):
        self.assertEqual(self.client.get("/api/drinks/mojito").get_json()["name"], "Mojito")
        res = self.client.get("/api/drinks/nope")
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.get_json(), {"error": "Drink not found"})
        self.assertEqual(self.client.get("/api/unknown").status_code, 404)

    def test_match_ignores_garnishes_and_is_case_insensitive(self):
        res = self.client.post("/api/match", json={"ingredients": ["gin", "TONIC WATER"]})
        data = res.get_json()
        self.assertIn("Gin & Tonic", [d["name"] for d in data["can_make"]])

    def test_match_almost_and_unlocks(self):
        data = self.client.post(
            "/api/match", json={"ingredients": ["Whiskey", "Simple Syrup"]}).get_json()
        self.assertEqual(data["can_make"], [])
        almost = {d["name"]: d["missing"] for d in data["almost"]}
        self.assertEqual(almost["Old Fashioned"], ["Angostura Bitters"])
        self.assertEqual(almost["Whiskey Sour"], ["Lemon Juice"])
        self.assertNotIn("Negroni", almost)  # shares nothing with what we have
        unlock_names = [u["ingredient"] for u in data["unlocks"]]
        self.assertIn("Angostura Bitters", unlock_names)

    def test_match_validates_body(self):
        self.assertEqual(self.client.post("/api/match", json={}).status_code, 400)
        self.assertEqual(self.client.post("/api/match", data="x").status_code, 400)

    def test_drinks_include_taste_profile(self):
        old_fashioned = self.client.get("/api/drinks/old-fashioned").get_json()
        self.assertEqual(old_fashioned["strength"], "strong")
        self.assertIn("bitter", old_fashioned["flavors"])
        self.assertEqual(old_fashioned["vibes"], ["rich"])

    def test_filter_by_flavor_strength_and_vibe(self):
        smoky = {d["name"] for d in self.client.get("/api/drinks?flavor=smoky").get_json()}
        self.assertEqual(smoky, {"Oaxaca Old Fashioned", "Rob Roy"})
        both = self.client.get("/api/drinks?flavor=sweet&flavor=creamy&vibe=rich").get_json()
        self.assertTrue(both)
        for d in both:
            self.assertTrue({"sweet", "creamy"} <= set(d["flavors"]))
            self.assertIn("rich", d["vibes"])
        light = self.client.get("/api/drinks?strength=light").get_json()
        self.assertTrue(light and all(d["strength"] == "light" for d in light))

    def test_profiles_vocabulary(self):
        data = self.client.get("/api/profiles").get_json()
        self.assertEqual(data["strengths"], ["light", "balanced", "strong"])
        self.assertIn("smoky", data["flavors"])
        self.assertEqual(data["vibes"], ["refreshing", "rich", "adventurous"])

    def test_catalog_reloads_when_seed_data_changes(self):
        self.db.execute("UPDATE catalog_meta SET value = %s WHERE key = %s", ("stale", "fingerprint"))
        self.db.execute("DELETE FROM drinks WHERE slug = %s", ("mojito",))
        self.db.commit()
        app = create_app({"TESTING": True, "SHARED_DB": self.db, "CLIENT_DIST": "/nonexistent"})
        self.assertEqual(app.test_client().get("/api/drinks/mojito").status_code, 200)

    def test_root_without_built_client(self):
        res = self.client.get("/")
        self.assertIn("running", res.get_json()["message"])


class SeedDataTest(unittest.TestCase):
    def test_every_drink_ingredient_exists(self):
        known = {n for names in INGREDIENTS.values() for n in names}
        for d in DRINKS:
            for name, _, _ in d["ingredients"]:
                self.assertIn(name, known, f"{d['name']} -> {name}")

    def test_every_drink_has_an_image_file(self):
        images = Path(__file__).resolve().parents[2] / "client" / "public"
        for d in DRINKS:
            self.assertTrue(d["image"], f"{d['name']} has no image")
            path = images / d["image"].lstrip("/")
            self.assertTrue(path.is_file(), f"{d['name']}: missing file {path}")

    def test_every_drink_has_a_valid_profile(self):
        from seed import validate_catalog
        validate_catalog()  # raises with a readable list of problems

    def test_slugs_unique(self):
        slugs = [d["slug"] for d in DRINKS]
        self.assertEqual(len(slugs), len(set(slugs)))


if __name__ == "__main__":
    unittest.main()
