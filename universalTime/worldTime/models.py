from django.db import models

# Create your models here.
class TimeZone(models.Model):
    title = models.CharField(max_length=255)
    zone = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    tz = models.CharField(max_length=255)

    def __str__(self):
        return self.title