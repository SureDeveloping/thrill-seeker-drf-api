from rest_framework import generics, permissions
from backend.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class LikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    filter_backends = [
            DjangoFilterBackend,
    ]

    filterset_fields = [
        'user__profile',
        'rating', 
    ]


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    See a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()