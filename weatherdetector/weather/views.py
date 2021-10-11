from django.shortcuts import render
import json
import urllib.request
from decouple import config

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        request_open_weather = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city.replace(' ', '%20')+'&appid='+config('OPEN_WEATHER_API_KEY')).read()
        json_data = json.loads(request_open_weather)
        data = {
            'city': city,
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp']) + 'K',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
        }
    else:
        data = {}
    return render(request, 'index.html', {'data': data})