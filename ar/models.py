from django.db import models

# Create your models here.
class Ayaah(models.Model):
    '''Ayaah model class'''
    image = models.ImageField(upload_to='ayahs',max_length=255,blank=True, null=True)
    content = models.TextField(blank=True, null=True)
