from django.urls import path
from . import views  # views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('trail/<slug:slug>/', views.trail_detail, name='trail_detail'), # Trail detail page
]
