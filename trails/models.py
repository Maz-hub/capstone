from django.db import models
from django.utils.text import slugify # For slug generation


# Trail model to store information about hiking trails
class Trail(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    map_embed_url = models.TextField(blank=True, null=True, help_text="Paste only the iframe src URL")
    latitude = models.FloatField(help_text="Latitude of the trail")
    longitude = models.FloatField(help_text="Longitude of the trail")
    distance = models.CharField(max_length=20, help_text="e.g. 14.5")
    duration = models.CharField(max_length=20, help_text="e.g. 1 hour, 4h 30min")
    difficulty = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

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
