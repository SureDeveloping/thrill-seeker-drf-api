from rest_framework import generics, permissions
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

    def get_serializer_class(self):
        print("Inside ContactFormList get_serializer_class")
        return self.serializer_class

class ContactFormDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve Update and Destroy contact form
    """
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        print("Inside ContactFormDetail get_serializer_class")
        return self.serializer_class

    def perform_update(self, serializer):
        print("Inside perform_update")
        instance = serializer.save()