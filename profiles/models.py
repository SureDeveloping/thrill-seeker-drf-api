from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_park = models.CharField(max_length=255, blank=True)
    favorite_ride = models.CharField(max_length=255, blank=True)
    userbio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', 
        default='media/images/profile_default_o6fet4', blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Profile'