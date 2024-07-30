from django.db import models
from django.core.validators import EmailValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import uuid


# Create your models here.

class ContactForm(models.Model):
    """
    Contact Form to send a message to the website owner
    """
    SUBJECT_CHOICES = [
        ('feedback', 'Feedback'),
        ('park_review_proposal', 'Park Review Proposal'),
        ('other', 'Other'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, validators=[EmailValidator()])
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    edit_token = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"

    def refresh_token(self):
        self.edit_token = uuid.uuid4()
        self.save()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Message send by {self.first_name} {self.last_name}"
