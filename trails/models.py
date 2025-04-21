from django.db import models

# Create your models here.

class Trail(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='trail_images/', blank=True, null=True)
    map_link = models.URLField(blank=True, null=True)
    start_location = models.CharField(max_length=200)
    ascent = models.IntegerField(help_text="Ascent in meters")
    descent = models.IntegerField(help_text="Descent in meters")
    distance = models.DecimalField(max_digits=5, decimal_places=2, help_text="Distance in kilometers")
    duration = models.DurationField(help_text="Expected duration (HH:MM)")
    difficulty = models.CharField(max_length=100)
    physical_requirements = models.TextField()

    def __str__(self):
        return self.name
