from django.db import models
from django.utils.text import slugify # For slug generation
from django.utils import timezone # For timezone-aware timestamps


# Trail model to store information about hiking trails
class Trail(models.Model):
    name = models.CharField(max_length=200) # Name of the trail
    slug = models.SlugField(unique=True, blank=True) # Slug for URL
    description = models.TextField() # Description of the trail
    image = models.ImageField(upload_to='trail_images/', blank=True, null=True)  # image for homepage
    canton = models.CharField(max_length=100)  # Canton for homepage display
    latitude = models.FloatField(help_text="Latitude of the trail") # Latitude for weather
    longitude = models.FloatField(help_text="Longitude of the trail") # Longitude for weather
    distance = models.CharField(max_length=20, help_text="e.g. 14.5") # Distance of the trail info-box
    duration = models.CharField(max_length=20, help_text="e.g. 1 hour, 4h 30min") # Duration of the trail info-box
    difficulty = models.CharField(max_length=100) # Difficulty of the trail info-box
    map_embed_url = models.TextField(blank=True, null=True, help_text="Paste only the iframe src URL") # Map embed URL for the trail
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


# TrailImage model to store multiple images for each trail
class TrailImage(models.Model):
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='trail_images/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.trail.name}"
    

class Comment(models.Model):
    trail = models.ForeignKey('Trail', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.name} on {self.trail.name}"
