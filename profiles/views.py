from django.db.models import Count
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer
from backend.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    """
    queryset = Profile.objects.annotate(
        ratings_count=Count('user__ratings', distinct=True),
        bucketlist_count=Count('user__bucketlist', distinct=True),
        like_count=Count('user__like', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        filters.OrderingFilter,
    ]
    ordering_fields = [
        'ratings_count',
        'bucketlist_count',
        'like_count',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        ratings_count=Count('user__ratings', distinct=True),
        bucketlist_count=Count('user__bucketlist', distinct=True),
        like_count=Count('user__like', distinct=True)
    )
    serializer_class = ProfileSerializer
