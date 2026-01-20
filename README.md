# Kanet Frontend

Kanet Frontend is a Django web UI that provides navigation and stop information screens, user authentication, and feedback flows. It is designed as a frontend surface that can be paired with backend services (for example, BLE distance data shown in the navigation screen).

## Features
- Authentication (register, login, logout).
- Main menu with links to stop navigation, schedules, and location.
- Stop listings and detail screens with dummy data placeholders.
- Navigation screen with voice prompts and BLE polling hooks.
- Feedback form flow.

## Tech Stack
- Django 5
- Tailwind CSS classes in templates
- SQLite for local development, PostgreSQL for production
- WhiteNoise for static asset serving

## Local Setup
```bash
python -m venv venv
# Windows
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and log in or register.

## Environment Variables
Create a `.env` file for production settings (optional in development):
- `PRODUCTION` (set to `true` to enable PostgreSQL)
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- `SCHEMA` (optional; defaults to `public`)

## Tests
```bash
python manage.py test
```

Note: some tests use Selenium and may require a compatible browser driver.

## Project Structure
- `kanet_frontend/` Django project settings and URLs
- `main/` Core app views and templates
- `templates/` Shared templates
- `static/` Static assets
