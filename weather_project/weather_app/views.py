from django.shortcuts import render
import requests

API_KEY = "986d36f8cb9cec168df0126f7355cbfe"

def weather_view(request):
    weather_data = None
    if request.method == "POST":
        city = request.POST.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": city,
                    "temperature": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "description": data["weather"][0]["description"]
                }
    
    return render(request, "index.html", {"weather": weather_data})
