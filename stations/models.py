from django.db import models
from django.contrib.auth.models import User

class Station(models.Model):
    title_ar = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    desc_ar = models.TextField()
    desc_en = models.TextField()
    video = models.FileField(upload_to='videos/')
    audio = models.FileField(upload_to='audios/') 
    order = models.PositiveIntegerField(unique=True)

class Guestbook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



    