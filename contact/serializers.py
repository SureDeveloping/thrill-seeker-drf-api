from rest_framework import serializers
from .models import ContactForm
import os
from django.core.mail import send_mail
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

ADMIN_EMAIL = os.environ.get("EMAIL_ADDRESS")


class ContactFormSerializer(serializers.ModelSerializer):
    """
    Contact form serializer.
    """

    class Meta:
        model = ContactForm
        fields = ["id", "first_name", "last_name",
            "email", "subject", "message",
            "created_at",
        ]

        read_only_fields = ["id", "created_at",
        ]

        extra_kwargs = {
            "first_name": {
                "error_messages": {"blank":  "This field is required"}
            },
            "last_name": {
                "error_messages": {"blank": "This field is required"}
            },
            "email": {
                "error_messages": {"blank": "This field is required"}
            },
            "subject": {
                "error_messages": {"blank": "This field is required"}
            },
            "message": {
                "error_messages": {"blank": "This field is required"}
            },
        }

    def validate_email(self, value):
        email_validator = EmailValidator()
        try:
            email_validator(value)
        except ValidationError:
            raise serializers.ValidationError("Enter a valid email address.")
        return value

    def validate_subject(self, value):
        if value not in dict(ContactForm.SUBJECT_CHOICES):
            raise serializers.ValidationError("Invalid subject choice.")
        return value

    def create(self, validated_data):
        """
        Creates contact form and send it via email to the admin.
        """
        contact = ContactForm.objects.create(**validated_data)

        # Send email
        subject = f"New Contact Form Submission: {contact.subject}"
        message = (
            f"First Name: {contact.first_name}\n"
            f"Last Name: {contact.last_name}\n"
            f"Email: {contact.email}\n"
            f"Subject: {contact.subject}\n"
            f"Message:\n{contact.message}\n"
            f"Created at: {contact.created_at}\n"         
        )
        
        try:
            send_mail(subject, message, contact.email, [ADMIN_EMAIL])
        except Exception as e:
            print(f"Failed to send Contact Form, Please try again {e}")

        return contact