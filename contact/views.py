from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from .models import ContactForm
from .serializers import ContactFormSerializer

class ContactFormList(generics.ListCreateAPIView):
    """
    List and create contact forms.
    """
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.AllowAny]

class ContactFormDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a contact form instance.
    """
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.AllowAny]

class FinalSubmitContactForm(APIView):
    """
    Handle the final submission of a contact form.
    """
    permission_classes = [permissions.AllowAny]

  