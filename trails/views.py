from django.shortcuts import render, get_object_or_404
from .models import Trail

def home(request):
    featured_trails = Trail.objects.all()[:6] # Get the first 6 trails
    return render(request, 'trails/home.html', {'featured_trails': featured_trails})

def trail_detail(request, slug):
    trail = get_object_or_404(Trail, slug=slug)
    return render(request, 'trails/trail_detail.html', {'trail': trail})
