from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import ContactForm
from .serializers import ContactFormSerializer

# Create your views here.

class ContactFormCreate(generics.CreateAPIView):
    """
    Creacte Contact form
    """
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['edit_token'] = str(response.data['edit_token'])
        return response

class ContactFormDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Request a contact form instance
    """
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'edit_token'

    def get_object(self):
        try:
            return ContactForm.objects.get(edit_token=self.kwargs['edit_token'])
        except ContactForm.DoesNotExist:
            raise NotFound('No contact form found with this edit token.')
