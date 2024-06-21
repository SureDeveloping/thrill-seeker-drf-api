from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Park
from .serializers import ParkSerializer

# Create your views here.


class ParkList(APIView):
    serializer_class = ParkSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
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
            serializer.save(author=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )