"""Tiny database layer.

PostgreSQL (via psycopg) is the real database. SQLite is supported too, so the
test suite and quick local demos run with zero setup:

    DATABASE_URL=postgresql://user:pass@localhost:5432/nook_pour   # default style
    DATABASE_URL=sqlite:///nook_pour.db                             # no server needed

All SQL in this project is written with %s placeholders; the SQLite adapter
translates them.
"""
import os
import sqlite3
from pathlib import Path

from flask import current_app, g

SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"
TABLES = ["drink_tags", "drink_steps", "drink_ingredients", "drinks", "ingredients", "catalog_meta"]  # drop order


def database_url():
    """Resolve the database URL from DATABASE_URL or the POSTGRESQL_* variables."""
    url = os.getenv("DATABASE_URL")
    if not url:
        user = os.getenv("POSTGRESQL_USER", "postgres")
        password = os.getenv("POSTGRESQL_PASSWORD", "")
        host = os.getenv("POSTGRESQL_HOST", "localhost")
        port = os.getenv("POSTGRESQL_PORT", "5432")
        name = os.getenv("POSTGRESQL_DB", "nook_pour")
        auth = f"{user}:{password}" if password else user
        url = f"postgresql://{auth}@{host}:{port}/{name}"
    if url.startswith("postgres://"):  # Render/Heroku style
        url = "postgresql://" + url[len("postgres://"):]
    return url


class Database:
    """Thin wrapper giving Postgres and SQLite the same small API."""

    def __init__(self, url):
        self.url = url
        if url.startswith("sqlite:"):
            self.dialect = "sqlite"
            path = url.split("sqlite:///", 1)[1] if "sqlite:///" in url else ":memory:"
            self.conn = sqlite3.connect(path or ":memory:", check_same_thread=False)
            self.conn.row_factory = lambda cur, row: {
                col[0]: row[i] for i, col in enumerate(cur.description)
            }
            self.conn.execute("PRAGMA foreign_keys = ON")
        else:
            import psycopg  # imported lazily so SQLite works without it
            from psycopg.rows import dict_row

            self.dialect = "postgres"
            self.conn = psycopg.connect(url, row_factory=dict_row)

    def _sql(self, sql):
        return sql.replace("%s", "?") if self.dialect == "sqlite" else sql

    def query(self, sql, params=()):
        cur = self.conn.execute(self._sql(sql), tuple(params))
        return cur.fetchall() if cur.description else []

    def one(self, sql, params=()):
        rows = self.query(sql, params)
        return rows[0] if rows else None

    def execute(self, sql, params=()):
        self.conn.execute(self._sql(sql), tuple(params))

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        self.conn.close()

    # --- schema helpers -------------------------------------------------
    def create_schema(self):
        sql = SCHEMA_PATH.read_text()
        if self.dialect == "sqlite":
            sql = sql.replace("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT")
            self.conn.executescript(sql)
        else:
            self.conn.execute(sql)
        self.commit()

    def drop_schema(self):
        for table in TABLES:
            suffix = " CASCADE" if self.dialect == "postgres" else ""
            self.conn.execute(f"DROP TABLE IF EXISTS {table}{suffix}")
        self.commit()


def get_db():
    """One connection per request, closed automatically at teardown."""
    if "db" not in g:
        shared = current_app.config.get("SHARED_DB")  # used by tests (in-memory SQLite)
        g.db = shared or Database(current_app.config["DATABASE_URL"])
    return g.db


def close_db(_exc=None):
    db = g.pop("db", None)
    if db is not None and not current_app.config.get("SHARED_DB"):
        db.close()
