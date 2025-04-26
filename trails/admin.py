from django.contrib import admin
from .models import Trail, TrailImage, Comment


# Register your models here.
# Registering the Trail model with custom admin options
@admin.register(Trail)
class TrailAdmin(admin.ModelAdmin):
    list_display = ("name", "distance", "duration", "difficulty")
    list_filter = ("difficulty",)
    search_fields = ("name", "description")

admin.site.register(TrailImage)

# Registering the Comment model with custom admin options
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "trail", "created_at")
    list_filter = ("trail", "created_at")
    search_fields = ("name", "text")
