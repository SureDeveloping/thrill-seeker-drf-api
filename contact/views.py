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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)