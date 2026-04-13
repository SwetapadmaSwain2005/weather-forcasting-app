# Weather Forecasting App

A Django weather forecasting web app built with Django 5.2.4.

## Setup

1. Clone the repository:
   ```bash
git clone https://github.com/SwetapadmaSwain2005/weather-forcasting-app.git
cd weather-forcasting-app
```
2. Create and activate a virtual environment:
   ```bash
python -m venv venv
# Windows
venv\Scripts\activate
```
3. Install dependencies:
   ```bash
pip install -r requirements.txt
```
4. Run migrations:
   ```bash
python weatherproject\manage.py migrate
```
5. Start the development server:
   ```bash
python weatherproject\manage.py runserver
```

## Deployment

This project is configured for deployment on platforms like Render or Railway using:
- `requirements.txt`
- `Procfile`
- `runtime.txt`

### Environment variables

Set these in production:
- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS` (e.g. `your-app.onrender.com`)

## GitHub

Source repository:
https://github.com/SwetapadmaSwain2005/weather-forcasting-app
