from django.shortcuts import render, get_object_or_404
from .models import Trail, TrailImage
import requests

def home(request):
    featured_trails = Trail.objects.all()
    return render(request, 'trails/home.html', {'featured_trails': featured_trails})



def trail_detail(request, slug):
    trail = get_object_or_404(Trail, slug=slug)
    images = TrailImage.objects.filter(trail=trail)

    # Weather API call
    weather_data = None
    try:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": trail.latitude,
                "longitude": trail.longitude,
                "current_weather": True
            }
        )
        data = response.json()
        weather_data = data.get("current_weather")
    except Exception as e:
        print("Weather API error:", e)

    return render(request, "trails/trail_detail.html", {
        "trail": trail,
        "images": images,
        "weather": weather_data
    })

def custom_404(request, exception):
    return render(request, 'trails/404.html', status=404)
