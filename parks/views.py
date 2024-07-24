from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Park
from .serializers import ParkSerializer
from backend.permissions import IsOwnerOrReadOnly

# Create your views here.


class ParkList(generics.ListCreateAPIView):
    serializer_class = ParkSerializer
    queryset = Park.objects.annotate(
        ratings_count=Count('rating', distinct=True),
        bucketlist_count=Count('bucketlist', distinct=True)
    ).order_by('-created_at')

    ordering_fields = [
        'bucketlist_count',
        'ratings_count',
        'thrill_factor',
        'overall_rating',
    ]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ParkDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParkSerializer
    queryset = Park.objects.annotate(
        ratings_count=Count('rating', distinct=True),
        bucketlist_count=Count('bucketlist', distinct=True)
    ).order_by('-created_at')

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsOwnerOrReadOnly(), permissions.IsAdminUser()]
        return [permissions.AllowAny()]
