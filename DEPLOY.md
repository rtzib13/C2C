Deployment checklist and minimal steps

Required environment variables
- SECRET_KEY: a strong secret key (required in production)
- DEBUG: false in production
- ALLOWED_HOSTS: comma-separated hostnames for your deployment (example: example.com,www.example.com)
- CONTACT_NOTIFICATION_EMAIL: email to receive form notifications
- DEFAULT_FROM_EMAIL: email to use as from-address for notifications
- EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS
- DATABASE_URL (optional): if using Postgres, set a DATABASE_URL like: postgres://USER:PASS@HOST:PORT/NAME

Install and prepare
1. Create and activate virtualenv

   python -m venv .venv
   source .venv/bin/activate

2. Install requirements

   pip install -r requirements.txt

3. Apply migrations and collect static files

   python manage.py migrate
   python manage.py collectstatic --noinput

4. Create a superuser

   python manage.py createsuperuser

Run (development)

   python manage.py runserver

Run (production example with gunicorn)

   gunicorn c2c_site.wsgi:application --bind 0.0.0.0:8000 --workers 3

Notes
- The project uses WhiteNoise for serving static files in simple deployments. For larger deployments prefer serving static files from S3/CloudFront or similar.
- Ensure `DEBUG` is `false` and `SECRET_KEY` is set in environment before exposing the site to the public.
- Use a production-ready database (Postgres) for concurrency and reliability.
