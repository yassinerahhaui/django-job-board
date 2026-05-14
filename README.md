# Django Job Board

A job board web application built with **Django** and **PostgreSQL**, featuring job listings, job posting & applications, user accounts, a blog module, and a contact page. The project includes a front-end template and static assets (JavaScript/CSS/SCSS).

> **Note**: This repository currently contains development settings (e.g., `DEBUG=True` and hard-coded credentials in `project/settings.py`). Before deploying, move secrets to environment variables and rotate any exposed credentials.

## Features

- Job listings (title, location, type, description, publish date, vacancies, salary, category, experience)
- Post a job & apply to jobs
- User accounts (login + profile redirect)
- Blog (posts, categories, tags, comments, search, recent posts)
- Contact page
- Static & media file handling (uploads)

## Tech Stack

- **Backend**: Django (see `requirements.txt`)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS/SCSS, JavaScript + Bootstrap

## Project Structure

- `project/` – Django project settings/urls/wsgi
- `accounts/` – user/account app
- `job/` – job board app
- `blog/` – blog app
- `contact/`, `home/` – site pages
- `templates/` – Django templates
- `static/` – static assets (CSS/JS/images)
- `media/` – uploaded media
- `Frontend-Template/` – front-end template resources

## Getting Started (Local Development)

### Prerequisites

- Python 3.x
- PostgreSQL 12+
- pip + virtualenv (recommended)

### 1) Clone the repo

```bash
git clone https://github.com/yassinerahhaui/django-job-board.git
cd django-job-board
```

### 2) Create & activate a virtual environment

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure PostgreSQL

This project is configured to use PostgreSQL in `project/settings.py`.

Create a database and user matching your local settings, or update `DATABASES` in `project/settings.py`.

Example (psql):

```sql
CREATE DATABASE jobboard;
CREATE USER admin WITH PASSWORD '123456';
GRANT ALL PRIVILEGES ON DATABASE jobboard TO admin;
```

Start PostgreSQL (helper script in repo):

```bash
sudo service postgresql start
```

### 5) Run migrations

```bash
python manage.py migrate
```

### 6) Create an admin user

```bash
python manage.py createsuperuser
```

### 7) Run the development server

```bash
python manage.py runserver
```

Open the app at:

- http://127.0.0.1:8000/

## Configuration & Security

For a production deployment, you should:

- Set `DEBUG=False`
- Move `SECRET_KEY`, database credentials, and email credentials to environment variables
- Set `ALLOWED_HOSTS`
- Configure static/media hosting appropriately

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit changes: `git commit -m "Add my feature"`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

## License

No license file is currently included in this repository. If you intend others to use/modify/distribute this project, consider adding a `LICENSE` file (e.g., MIT).
