from rest_framework import generics, permissions
from .models import ContactForm
from .serializers import ContactFormSerializer
from backend.permissions import IsOwnerOrTokenValid


# Create your views here.

class ContactFormList(generics.ListCreateAPIView):
    """
    List create contact form
    """
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.AllowAny]

class ContactFormDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve Update and Destroy contact form
    """
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [IsOwnerOrTokenValid]

    def perform_update(self, serializer):
        instance = serializer.save()