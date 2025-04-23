from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('trail/', lambda request: redirect('/')), # Redirect to homepage
    path('trail/<slug:slug>/', views.trail_detail, name='trail_detail'), # Trail detail page 
]
