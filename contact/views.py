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

    def post(self, request, pk=None):
        try:
            contact_form = ContactForm.objects.get(pk=pk)
            return Response({'status': 'submitted', 'message': 'Contact form has been finally submitted.'}, status=status.HTTP_200_OK)
        except ContactForm.DoesNotExist:
            return Response({'error': 'Contact form not found'}, status=status.HTTP_404_NOT_FOUND)