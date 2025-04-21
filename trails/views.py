from django.shortcuts import render
from .models import Trail 

# Create your views here.
def home(request):
    featured_trails = Trail.objects.all()[:4]
    return render(request, 'trails/home.html', {'featured_trails': featured_trails})
