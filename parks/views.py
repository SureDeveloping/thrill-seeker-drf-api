from rest_framework import generics, permissions
from .models import Park
from .serializers import ParkSerializer
from backend.permissions import IsOwnerOrReadOnly

# Create your views here.

class ParkList(generics.ListCreateAPIView):
    serializer_class = ParkSerializer
    queryset = Park.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ParkDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParkSerializer
    queryset = Park.objects.all()

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsOwnerOrReadOnly(), permissions.IsAdminUser()]
        return [permissions.AllowAny()]