from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Park
from .serializers import ParkSerializer
from backend.permissions import IsOwnerOrReadOnly

# Create your views here.


class ParkList(APIView):
    serializer_class = ParkSerializer
    permission_classes = [
        permissions.IsAdminUser
    ]

    def get(self, request):
        parks = Park.objects.all()
        serializer = ParkSerializer(
            parks, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_superuser:
            return Response(
                {'detail': 'Only superusers can create new parks.'},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = ParkSerializer(
            data=request.data, context={'request': request}
        )

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class ParkDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ParkSerializer

    def get_object(self, pk):
        try:
            park = Park.objects.get(pk=pk)
            self.check_object_permissions(self.request, park)
            return park
        except Park.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        park = self.get_object(pk)
        serializer = ParkSerializer(
            park, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        park = self.get_object(pk)

        if not request.user.is_superuser:
            return Response(
                {'detail': 'Only superusers can edit this park.'},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = ParkSerializer(
            park, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        park = self.get_object(pk)
        park.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )