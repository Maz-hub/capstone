from django.shortcuts import render, get_object_or_404, redirect
from .models import Trail, TrailImage, Comment
from django.core.paginator import Paginator
from .forms import CommentForm
import requests

#
def home(request):
    difficulty = request.GET.get('difficulty')
    
    if difficulty:
        featured_trails = Trail.objects.filter(difficulty=difficulty)
    else:
        featured_trails = Trail.objects.all()
        
    return render(request, 'trails/home.html', {
        'featured_trails': featured_trails,
        'selected_difficulty': difficulty
    })


# Trail detail page
def trail_detail(request, slug):
    trail = get_object_or_404(Trail, slug=slug)
    images = TrailImage.objects.filter(trail=trail)
    comments = Comment.objects.filter(trail=trail).order_by("-created_at")

    paginator = Paginator(comments, 5)  # Show 5 comments per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number) # Get the comments for the current page

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

    # Comment form handling
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.trail = trail
            new_comment.save()
            return redirect("trail_detail", slug=slug)
    else:
        form = CommentForm()

    return render(request, "trails/trail_detail.html", {
        "trail": trail,
        "images": images,
        "weather": weather_data,
        "page_obj": page_obj, # Paginated comments
        "form": form
    })


