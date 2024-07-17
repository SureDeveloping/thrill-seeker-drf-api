from django.db import models
from django.contrib.auth.models import User
from parks.models import Park
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Rating(models.Model):
    """
    Rating model, related to User and Park
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    park = models.ForeignKey(Park, on_delete=models.CASCADE)
    explanation = models.TextField(blank=False)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'park']

    def __str__(self):
        return self.explanation