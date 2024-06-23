from django.db import models
from django.contrib.auth.models import User
from parks.models import Park

# Create your models here.

class Bucketlist(models.Model):
    """
    Bucketlist related to the "user" and "park" model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    park = models.ForeignKey(
        Park, related_name='bucketlist', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'park']

    def __str__(self):
        return f'{self.user} {self.park}'
