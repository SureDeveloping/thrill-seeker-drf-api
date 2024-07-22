from django.db import IntegrityError
from rest_framework import serializers
from bucketlist.models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    """
    Serializer for the Bucketlist model
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Bucketlist
        fields = ['id', 'user', 'park', 'created_at']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Park is already on your bucket list'
            })
