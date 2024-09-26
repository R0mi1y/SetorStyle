from django.db import models

class Sector(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    banners = models.ManyToManyField('Banner')
    
    
class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='banners/')