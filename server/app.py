"""Nook & Pour API (Flask + PostgreSQL)."""
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from catalog import INGREDIENT_CATEGORIES, list_ingredients, load_drinks, match_drinks
from seed_data import FLAVORS, STRENGTHS, VIBES
from db import Database, close_db, database_url, get_db

load_dotenv()

CLIENT_DIST = Path(__file__).resolve().parent.parent / "client" / "dist"


def create_app(config=None):
    app = Flask(__name__, static_folder=None)
    app.config["DATABASE_URL"] = database_url()
    app.config["CLIENT_DIST"] = CLIENT_DIST
    app.json.sort_keys = False
    app.json.ensure_ascii = False
    if config:
        app.config.update(config)

    CORS(app, resources={r"/api/*": {"origins": os.getenv("CORS_ORIGINS", "*")}})
    app.teardown_appcontext(close_db)

    with app.app_context():
        init_database(app)

    register_routes(app)
    return app


def init_database(app):
    """Create tables if needed, and (re)load the catalog when it's empty or seed_data.py changed.

    Everything in this database comes from seed_data.py (users' bars and favorites live in
    their browsers), so rebuilding it on a catalog change is safe.
    """
    from seed import catalog_fingerprint, seed_database

    db = app.config.get("SHARED_DB") or Database(app.config["DATABASE_URL"])
    try:
        db.create_schema()
        stored = db.one("SELECT value FROM catalog_meta WHERE key = %s", ("fingerprint",))
        if stored is None or stored["value"] != catalog_fingerprint():
            seed_database(db, reset=True)
            app.logger.info("Catalog changed — reloaded drinks from seed_data.py.")
    finally:
        if not app.config.get("SHARED_DB"):
            db.close()


def register_routes(app):
    @app.get("/api/health")
    def health():
        n = get_db().one("SELECT COUNT(*) AS n FROM drinks")["n"]
        return jsonify({"status": "ok", "drinks": n})

    @app.get("/api/ingredients")
    def get_ingredients():
        return jsonify(
            {
                "categories": [{"key": k, "label": v} for k, v in INGREDIENT_CATEGORIES.items()],
                "ingredients": list_ingredients(get_db()),
            }
        )

    @app.get("/api/drinks")
    def get_drinks():
        search = request.args.get("q", "").strip() or None
        kind = request.args.get("kind", "").strip() or None
        # e.g. /api/drinks?flavor=sweet&flavor=creamy&strength=balanced&vibe=rich
        flavors = [f for f in request.args.getlist("flavor") if f.strip()]
        vibes = [v for v in request.args.getlist("vibe") if v.strip()]
        strength = request.args.get("strength", "").strip() or None
        return jsonify(load_drinks(get_db(), search=search, kind=kind,
                                   flavors=flavors, vibes=vibes, strength=strength))

    @app.get("/api/profiles")
    def get_profiles():
        """The taste-profile vocabulary, for the client and the future AI bartender."""
        return jsonify({"flavors": FLAVORS, "strengths": STRENGTHS, "vibes": VIBES})

    @app.get("/api/drinks/<slug>")
    def get_drink(slug):
        found = load_drinks(get_db(), slug=slug)
        if not found:
            return jsonify({"error": "Drink not found"}), 404
        return jsonify(found[0])

    @app.post("/api/match")
    def match():
        body = request.get_json(silent=True) or {}
        names = body.get("ingredients")
        if not isinstance(names, list):
            return jsonify({"error": 'Send JSON like {"ingredients": ["Gin", "Tonic Water"]}'}), 400
        return jsonify(match_drinks(load_drinks(get_db()), names))

    @app.errorhandler(HTTPException)
    def http_error(err):
        if request.path.startswith("/api/"):
            return jsonify({"error": err.description}), err.code
        return err

    @app.errorhandler(Exception)
    def server_error(err):
        app.logger.exception(err)
        return jsonify({"error": "Something went wrong on our end."}), 500

    # In production Flask also serves the built React app from client/dist.
    # In development, Vite serves the client and proxies /api here.
    @app.get("/", defaults={"path": ""})
    @app.get("/<path:path>")
    def client(path):
        dist = Path(app.config["CLIENT_DIST"])
        if path.startswith("api/"):
            return jsonify({"error": "Not found"}), 404
        if not (dist / "index.html").exists():
            return jsonify({"message": "Nook & Pour API is running. Start the client with `npm run dev`."})
        if path and (dist / path).is_file():
            return send_from_directory(dist, path)
        return send_from_directory(dist, "index.html")


if __name__ == "__main__":
    create_app().run(
        port=int(os.getenv("PORT", "5000")),
        debug=os.getenv("FLASK_DEBUG", "1") == "1",
    )
