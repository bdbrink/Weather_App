import datetime
import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    API_KEY = "bd8a0a0778426c96165226c224399ce2"
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    forecast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"

    if request.method == "POST":
        city1 = request.POST['city1']
        city2 = request.get('city2', None)
    else:
        return render(request, "weather_app/index.html")

def fetch_weather_forecast(city, api_key, current_weather_url, forecast_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    lat, lon = response