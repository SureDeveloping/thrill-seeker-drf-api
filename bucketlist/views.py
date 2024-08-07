from rest_framework import generics, permissions
from backend.permissions import IsOwnerOrReadOnly
from bucketlist.models import Bucketlist
from bucketlist.serializers import BucketlistSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your models here.


class BucketlistList(generics.ListCreateAPIView):
    """
    Bucketlist related to the "user" and "park" model
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BucketlistSerializer
    queryset = Bucketlist.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['park', 'user__profile']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BucketlistDetail(generics.RetrieveDestroyAPIView):
    """
    See a Bucketlist item or delete Bucketlist item by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BucketlistSerializer
    queryset = Bucketlist.objects.all()
