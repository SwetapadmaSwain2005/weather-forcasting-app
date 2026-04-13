import os
import requests
import datetime

from django.contrib import messages
from django.shortcuts import render

# View function for the homepage
def home(request):
    default_city = 'Indore'
    search_history = request.session.get('search_history', [])

    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
    else:
        city = request.GET.get('city', '').strip()

    if not city:
        city = request.session.get('last_city', default_city)

    api_key = os.environ.get('OPENWEATHER_API_KEY', '')
    weather_data = {}

    if not api_key:
        messages.error(request, 'OPENWEATHER_API_KEY is not configured. Set this environment variable before running the app.')
    else:
        try:
            url = 'https://api.openweathermap.org/data/2.5/weather'
            params = {
                'q': city,
                'appid': api_key,
                'units': 'metric',
            }
            response = requests.get(url, params=params, timeout=10)
            data = response.json()

            if response.status_code != 200:
                raise ValueError(data.get('message', 'Unable to fetch weather data'))

            weather = data['weather'][0]
            main = data['main']
            wind = data.get('wind', {})
            sys = data.get('sys', {})

            weather_data = {
                'city': data.get('name', city),
                'country': sys.get('country', ''),
                'description': weather.get('description', '').title(),
                'icon': weather.get('icon', '01d'),
                'temp': round(main.get('temp', 0)),
                'feels_like': round(main.get('feels_like', 0)),
                'humidity': main.get('humidity', 0),
                'pressure': main.get('pressure', 0),
                'wind_speed': wind.get('speed', 0),
                'day': datetime.date.today(),
                'background_url': f'https://source.unsplash.com/1600x900/?{city},weather',
            }

            request.session['last_city'] = weather_data['city']

            if weather_data['city'] in search_history:
                search_history.remove(weather_data['city'])
            search_history.insert(0, weather_data['city'])
            request.session['search_history'] = search_history[:5]

        except (requests.RequestException, ValueError, KeyError) as exc:
            messages.error(request, f'Could not load weather for "{city}". {exc}')

    if not weather_data:
        weather_data = {
            'city': default_city,
            'country': 'IN',
            'description': 'Clear Sky',
            'icon': '01d',
            'temp': 25,
            'feels_like': 25,
            'humidity': 50,
            'pressure': 1013,
            'wind_speed': 3.5,
            'day': datetime.date.today(),
            'background_url': 'https://images.pexels.com/photos/1118873/pexels-photo-1118873.jpeg?auto=compress&cs=tinysrgb&w=1600',
        }
        request.session['last_city'] = default_city

    return render(request, 'weatherapp/index.html', {
        'search_history': search_history,
        **weather_data,
    })

