from django.urls import path
from . import views  # views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
]
