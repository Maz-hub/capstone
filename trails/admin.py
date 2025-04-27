from django.contrib import admin
from django import forms
from .models import Trail, TrailImage, Comment


# Custom form for TrailAdmin
class TrailAdminForm(forms.ModelForm):
    class Meta:
        model = Trail
        fields = '__all__'
        widgets = {
            'map_embed_url': forms.URLInput(attrs={'placeholder': 'e.g., https://s.geo.admin.ch/...'}),
        }

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
