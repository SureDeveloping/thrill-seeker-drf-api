from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Park(models.Model):
    """
    Parking model, related to the "author", superuser
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='', blank=True
    )
    # Address fields
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)

    # Good to know
    opening_hours = models.TextField(max_length=255, blank=True)
    entrance_fees = models.TextField(max_length=255, blank=True)

    # Other interesting data 
    total_number_of_rides = models.IntegerField(blank=True, null=True)
    total_number_of_roller_coasters = models.IntegerField(blank=True, null=True)
    total_number_of_shows = models.IntegerField(blank=True, null=True)
    total_number_of_children_rides = models.IntegerField(blank=True, null=True)
    park_size = models.FloatField(blank=True, null=True)

    # Ratings
    family_friendliness = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    thrill_factor = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    overall_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.name}'