from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Park(models.Model):
    """
    Park model, related to the "user", superuser
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='', blank=True
    )
    website = models.URLField(max_length=200, blank=True)
    total_number_of_rides = models.IntegerField(blank=True, null=True)
    total_number_of_coasters = models.IntegerField(blank=True, null=True)

    # Ratings
    thrill_factor = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    overall_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.name}'