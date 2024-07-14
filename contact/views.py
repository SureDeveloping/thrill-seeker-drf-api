from rest_framework import generics, permissions, status
from rest_framework.response import Response
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

class FinalSubmitContactForm(generics.GenericAPIView):
    """
    Final submit of contact form
    """
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)