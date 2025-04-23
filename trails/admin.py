from django.contrib import admin
from .models import Trail, TrailImage


# Register your models here.

@admin.register(Trail)
class TrailAdmin(admin.ModelAdmin):
    list_display = ("name", "distance", "duration", "difficulty")
    list_filter = ("difficulty",)
    search_fields = ("name", "description")

admin.site.register(TrailImage)