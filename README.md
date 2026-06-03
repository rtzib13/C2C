# Cummings 2 Clean Django Website

Professional website for residential and commercial cleaning services.

## Features

- Home, Services, About, Contact, and Careers pages
- Quote request form saved to database and emailed to owner
- Career application form saved to database and emailed to owner
- Django admin access for all submissions
- Navigation links mapped to valid routes to avoid internal 404s

## Local Setup

1. Create and activate a virtual environment.
2. Install dependencies:

   /Users/randytzib/Projects/C2C/.venv/bin/python -m pip install -r requirements.txt

3. Apply migrations:

   /Users/randytzib/Projects/C2C/.venv/bin/python manage.py migrate

4. Start server:

   /Users/randytzib/Projects/C2C/.venv/bin/python manage.py runserver

## Email Delivery Setup

Django reads email settings from environment variables in `c2c_site/settings.py`.

1. Copy `.env.example` values into your shell environment.
2. Set `EMAIL_HOST_PASSWORD` to a valid Gmail App Password.
3. Keep `CONTACT_NOTIFICATION_EMAIL` as the owner mailbox.

If SMTP credentials are missing or invalid:

- Submissions are still saved to the database.
- The UI displays a warning saying email delivery is not configured.

## Branding assets

Replace the placeholder images with your exact client assets to perfectly match the mockup:

- `static/images/logo.svg` — header tile/logo. Replace with the provided high-resolution logo (SVG/PNG).
- `static/images/hero.jpg` — hero background image. Add the client's hero photo at this path; the CSS will fall back to an online placeholder if the file is missing.

After adding assets, refresh the page. The header logo and hero should match the client's supplied images and color scheme.

## Admin Access

Create an admin user:

/Users/randytzib/Projects/C2C/.venv/bin/python manage.py createsuperuser

Then open:

- /admin/

Models available in admin:

- Quote Requests
- Career Applications
