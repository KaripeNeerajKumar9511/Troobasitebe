# Trooba CMS backend (Django)

REST API for the public site and the Next.js admin panel. **Does not send email.** SMTP stays in the Frontend Next.js app (`Frontend/src/lib/assessment/mail.ts`).

## Setup

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Create a PostgreSQL database and user matching the `DB_*` values in `.env` (this project does not use SQLite):

```sql
CREATE USER trooba WITH PASSWORD 'trooba';
CREATE DATABASE trooba OWNER trooba;
GRANT ALL PRIVILEGES ON DATABASE trooba TO trooba;
```

Edit [`backend/.env`](.env) if your host, user, or password differ. Then:

```bash
python manage.py migrate
python manage.py seed_cms
python manage.py runserver 8000
```

- API health: http://localhost:8000/api/health/
- Public site bundle: http://localhost:8000/api/public/site/
- Admin login: `POST /api/admin/login/` with `{ "email", "password" }`
- Django admin (optional): http://localhost:8000/django-admin/

Default seed login: `ADMIN_EMAIL` / `ADMIN_PASSWORD` from `.env`.
