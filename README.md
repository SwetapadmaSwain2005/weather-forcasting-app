# Weather Forecasting App

A Django weather forecasting app that fetches live weather data from the OpenWeather API.

## Features

- Search weather by city name
- Live temperature, humidity, pressure, wind speed, and description
- Retains your last searches in session history
- Uses a dynamic background image for the selected city
- Ready for deployment with `Procfile`, `requirements.txt`, and `runtime.txt`

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
4. Set your OpenWeather API key:
   - Create an account at https://openweathermap.org/
   - Generate an API key
   - Set it in your environment:
     ```bash
set OPENWEATHER_API_KEY=your_api_key_here
```
5. Run migrations:
   ```bash
python weatherproject\manage.py migrate
```
6. Start the development server:
   ```bash
python weatherproject\manage.py runserver
```

## Running locally with API key

The weather search requires `OPENWEATHER_API_KEY`. Without it, the app runs with fallback data and displays an error message.

## Deployment

This project is configured for deployment on platforms like Render or Railway using:
- `requirements.txt`
- `Procfile`
- `runtime.txt`

### Environment variables for production

Set these in production:
- `OPENWEATHER_API_KEY`
- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS=your-host.example.com`

## Repository

Source repository:
https://github.com/SwetapadmaSwain2005/weather-forcasting-app
