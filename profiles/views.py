from django.db.models import Count
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from backend.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.


class ProfileList(generics.ListAPIView):
    """
    List all profiles
    """
    queryset = Profile.objects.annotate(
        ratings_count=Count('user__rating', distinct=True),
        bucketlist_count=Count('user__bucketlist', distinct=True),
        like_count=Count('user__like', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer

    filter_backends = [
        filters.OrderingFilter,
    ]

    ordering_fields = [
        'ratings_count',
        'bucketlist_count',
        'like_count',
    ]
    permission_classes = [IsAuthenticated]

class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        ratings_count=Count('user__rating', distinct=True),
        bucketlist_count=Count('user__bucketlist', distinct=True),
        like_count=Count('user__like', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer