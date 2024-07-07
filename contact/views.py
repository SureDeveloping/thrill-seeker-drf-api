from rest_framework import generics
from .models import ContactForm
from .serializers import ContactFormSerializer

# Create your views here.

class ContactFormList(generics.ListCreateAPIView):
    """
    List create contact form
    """
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.AllowAny]
