---
description: Migrate SQLite database to PostgreSQL using Flask-Migrate
---

# Migration Workflow

This workflow guides you through switching the project's database from SQLite to PostgreSQL.
It assumes you have PostgreSQL installed locally (or have access to a remote instance) and that you have updated the `.env` file with the correct `DATABASE_URL`.

## Steps

1. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```
   // turbo
2. **Verify environment variables**
   Ensure `.env` contains a valid PostgreSQL URL, e.g.
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/marketpulse
   FLASK_APP=app.py
   FLASK_ENV=development
   ```
3. **Initialize migration repository**
   ```bash
   flask db init
   ```
   // turbo
4. **Create an initial migration**
   ```bash
   flask db migrate -m "Initial migration to PostgreSQL"
   ```
   // turbo
5. **Apply the migration to the PostgreSQL database**
   ```bash
   flask db upgrade
   ```
   // turbo
6. **Run the application**
   ```bash
   flask run
   ```
   // turbo

## Notes
- If you encounter compilation errors installing `psycopg2-binary`, ensure you have a C compiler installed (e.g., `build-essential` on Linux or Visual C++ Build Tools on Windows).
- After the migration, you can remove the old `organic_shop.db` SQLite file if it is no longer needed.
- For further schema changes, repeat steps 4‑5.
