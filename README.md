<div align="center">
  <img src="client/public/images/logo.png" alt="Nook & Pour logo" width="140" />

# Nook & Pour

**Tell it what's in your cabinet. It tells you what to pour.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

Nook & Pour is a full-stack cocktail app. Pick the spirits, mixers and garnishes you have, and it shows:

- **Ready to pour:** every drink you can make right now
- **Almost there:** drinks you're one or two ingredients away from, with what's missing
- **Best next buy:** the single bottle that would unlock the most new drinks

You can also browse and search all recipes (cocktails and shots), open a full recipe page with measurements, and save favorites.

## Tech stack

| Layer    | Tech |
| -------- | ---- |
| Frontend | React 18, React Router 7, React Bootstrap, Vite |
| Backend  | Python, Flask, REST API |
| Database | PostgreSQL (via psycopg), with plain SQL in `server/schema.sql` |
| Testing  | pytest (runs on in-memory SQLite, so no Postgres needed for tests) |

## Getting started

### Prerequisites

- Node.js 18+
- Python 3.10+
- PostgreSQL 14+ running locally (or a hosted URL from Neon, Supabase, Render, etc.)

### 1. Install

```bash
git clone git@github.com:Drew-Andersen/Nook-Pour.git
cd Nook-Pour

python3 -m venv server/venv
source server/venv/bin/activate          # Windows: server\venv\Scripts\activate

npm run setup                            # pip + npm installs for server, root and client
```

### 2. Configure the database

```bash
createdb nook_pour
cp server/.env.example server/.env       # then fill in your Postgres user/password
```

`server/.env` accepts either a single `DATABASE_URL` or the separate `POSTGRESQL_*` values.

> No Postgres handy? Set `DATABASE_URL=sqlite:///nook_pour.db` for a quick zero-setup demo.

### 3. Run it

```bash
npm run dev
```

- React app: http://localhost:5173
- Flask API: http://localhost:5000 (Vite proxies `/api` to it)

On first start the API creates the tables and loads the starter recipes automatically. To reset the data later, run `npm run seed`.

## Scripts (from the project root)

| Command         | What it does |
| --------------- | ------------ |
| `npm run dev`   | Runs Flask and Vite together |
| `npm run seed`  | Drops and reloads all tables from `server/seed_data.py` |
| `npm test`      | Runs the API test suite |
| `npm run lint`  | Lints the React code |
| `npm run build` | Builds the React app into `client/dist` |
| `npm start`     | Production server: gunicorn serves the API **and** the built React app |

## API

| Method | Route                  | Description |
| ------ | ---------------------- | ----------- |
| GET    | `/api/health`          | Status and drink count |
| GET    | `/api/ingredients`     | Ingredients plus category labels |
| GET    | `/api/drinks`          | All drinks. Optional `?q=gin` (name or ingredient) and `?kind=shot` |
| GET    | `/api/drinks/:slug`    | One drink, e.g. `/api/drinks/old-fashioned` |
| POST   | `/api/match`           | Body `{"ingredients": ["Gin", "Tonic Water"]}` → `can_make`, `almost`, `unlocks` |

Optional ingredients (garnishes, salt rims) are shown in recipes but never stop a drink from matching.

## Project structure

```
client/                 React app (Vite)
  src/pages/            Home, My Bar, What Can I Make?, All Drinks, Drink detail, Favorites, 404
  src/components/       DrinkCard, DrinkModal, Recipe, Header, ...
  src/lib/api.js        All fetch calls in one place
server/
  app.py                Flask app + routes (also serves client/dist in production)
  catalog.py            Queries and the matching logic
  db.py                 Postgres/SQLite connection wrapper
  schema.sql            Table definitions
  seed_data.py          The recipe catalog: add drinks here
  tests/                API tests
```

### Adding a drink

Add an entry to `DRINKS` in `server/seed_data.py` (and any new ingredient to `INGREDIENTS`), drop an image in `client/public/images/` if you have one, then run `npm run seed`. Drinks without an image show their emoji.

## Deploying (single service)

Any host that runs Python and Node works (Render, Railway, Fly.io):

- **Build command:** `pip install -r server/requirements.txt && npm run build`
- **Start command:** `npm start` (or `cd server && gunicorn 'app:create_app()'`)
- **Environment:** `DATABASE_URL` pointing at your Postgres database

Flask serves the built React app and the API from the same URL, so there's no CORS setup to manage.

## Roadmap

### MVP (current focus)

- [x] Ingredient selection, persisted between visits
- [x] Matching with "almost there" and "best next buy"
- [x] PostgreSQL database
- [x] Search, filters, recipe pages, favorites, 404 page
- [x] Loading and error states
- [ ] Polish the app
- [ ] Deploy and release to the public

### Future development (after the MVP is public)

- [ ] **User accounts / log in:** save each user's bar and favorites to their account so they
  sync everywhere. (Today they're stored in the browser's localStorage, so they stay on one device.)
- [ ] **AI agent:** an assistant built into Nook & Pour.
- [ ] Submit your own recipes
- [ ] **Apple App Store app:** release Nook & Pour as an iOS app, possibly priced at $0.99.

## License

MIT. See `LICENSE`.

## Contact

**Drew Andersen** · [GitHub](https://github.com/Drew-Andersen) · [Email](mailto:andrewtandersen@gmail.com)
