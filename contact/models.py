from django.db import models
from django.core.validators import EmailValidator
from django.core.mail import send_mail
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
    edit_token = models.UUIDField(default=uuid.uuid1, editable=False, unique=True)



    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Message send by {self.first_name} {self.last_name}"


@receiver(post_save, sender=ContactForm)
def send_contact_email(sender, instance, created, **kwargs):
    if created:
        subject = instance.subject
        message = (
            f"You have received a new message from the contact form:\n\n"
            f"Name: {instance.first_name} {instance.last_name}\n"
            f"Email: {instance.email}\n"
            f"Subject: {instance.subject}\n\n"
            f"Message:\n{instance.message}\n"
            f"Created at: {instance.created_at}\n"
        )
        from_email = instance.email
        to_email = [settings.ADMIN_EMAIL]

        send_mail(subject, message, from_email, to_email)

        