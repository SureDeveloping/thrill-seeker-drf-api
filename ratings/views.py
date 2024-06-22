from rest_framework import generics, permissions, serializers
from django.db import IntegrityError
from backend.permissions import IsOwnerOrReadOnly
from .models import Rating
from .serializers import RatingSerializer, RatingDetailSerializer

# Create your views here.


class RatingList(generics.ListCreateAPIView):
    """
    List and create rating if user is logged in.
    """
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        park = serializer.validated_data['park']

        existing_rating = Rating.objects.filter(user=user, park=park).exists()
        if existing_rating:
            raise serializers.ValidationError({
                'detail': 'You have already rated this park.'
            })

        serializer.save(user=user)


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update or delete a rating by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingDetailSerializer
    queryset = Rating.objects.all()