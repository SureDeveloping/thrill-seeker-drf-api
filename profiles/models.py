from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_park = models.CharField(max_length=255, blank=True)
    favorite_ride = models.CharField(max_length=255, blank=True)
    userbio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(
        upload_to = 'images/', default='../profile_default_o7qozg'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)