# Softuni_exam

Project setup
1. Clone the repo

  git clone https://github.com/deividid/Softuni_exam/tree/main/djangoProject

2. Open the project
3. Install dependencies

  pip install psycopg2

4. Change DB settings in settings.py

DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql",
          "NAME": "your_db_name",
          "USER": "your_username",
          "PASSWORD": "your_pass",
          "HOST": "127.0.0.1",
          "PORT": "5432",
      }
  }
6. Run the migrations

  python manage.py migrate

6. Run the project

  python manage.py runserver
