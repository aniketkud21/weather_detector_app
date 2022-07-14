import imp
import sys
from django.shortcuts import render
import json
import urllib

# Create your views here.

def index(request):
    if(request.method == 'POST'):
        city = request.POST['city']
        api_key = '39b82b1ed5507b459b5a63c622175cff'
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key+'').read()
        json_data = json.loads(res)
        data = {
            'city': city,
            'country_code': str(json_data['sys']['country']),
            'latitude': str(json_data['coord']['lat']),
            'temperature': str(json_data['main']['temp']),
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity'])
        }
    else:
        city=''
        data={}
        
    return render(request, 'index.html', data)
