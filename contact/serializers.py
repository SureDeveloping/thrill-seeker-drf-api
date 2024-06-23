from rest_framework import serializers
from .models import ContactForm

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

        read_only_fields = ["id", "created_at"]

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

        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        """
        Creates contact form and send it via email to the admin.
        """
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        email = validated_data["email"]
        subject = validated_data["subject"]
        message = validated_data["message"]

        contact = ContactForm.objects.create(
            first_name=first_name, last_name=last_name, email=email,
            subject=subject, message=message
        )

        return contact