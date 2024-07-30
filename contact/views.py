from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import ContactForm
from .serializers import ContactFormSerializer


class ContactFormCreate(generics.CreateAPIView):
    """
    Create a new contact form and provide an edit token.
    """
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = serializer.data
        response_data['edit_token'] = serializer.instance.edit_token
        return Response(
            response_data, status=status.HTTP_201_CREATED, headers=headers)


class ContactFormUpdate(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update and delete an existing
    contact form using the provided edit token.
    """
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'edit_token'

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve the contact form data.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        Update the contact form data.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Refresh the token after successful update
        instance.refresh_token()

        response_data = serializer.data
        response_data['edit_token'] = str(instance.edit_token)
        return Response(response_data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContactFormList(generics.ListAPIView):
    """
    List all contact forms.
    """
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.IsAdminUser]

    def list(self, request, *args, **kwargs):
    if not request.user.is_staff:
        return Response(
            {"detail": "You do not have permission to this data."},
            status=status.HTTP_403_FORBIDDEN
        )
    return super().list(request, *args, **kwargs)