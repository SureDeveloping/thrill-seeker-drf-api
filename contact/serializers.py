from rest_framework import serializers
from .models import ContactForm


class ContactFormSerializer(serializers.ModelSerializer):
    """
    Contact form serializer.
    """

    class Meta:
        model = ContactForm
        fields = [
            "id", "first_name", "last_name",
            "email", "subject", "message",
            "created_at",
        ]
        read_only_fields = [
            "id", "created_at",
        ]

    def validate_subject(self, value):
        if value not in dict(ContactForm.SUBJECT_CHOICES):
            raise serializers.ValidationError("Invalid subject choice.")
        return value

    extra_kwargs = {
        "first_name": {
            "error_messages": {"blank": "This field is required"}
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
