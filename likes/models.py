from django.db import models
from django.contrib.auth.models import User
from ratings.models import Rating

# Create your models here.

class Like(models.Model):
    """
    Like model, related to 'user' and 'rating'
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.ForeignKey(
        Rating, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'rating']

    def __str__(self):
        return f'{self.user} {self.rating}'
