from django.db import IntegrityError
from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Rating model
    """
    user = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_picture = serializers.ReadOnlyField(
        source='user.profile.profile_picture.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Rating
        fields = [
            'id', 'user', 'is_owner', 'park', 'rating', 
            'last_visisted_at','explanation', 
            'profile_id', 'profile_picture',
            'created_at', 'updated_at', 
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Duplicate rating for this park by this user'
            })

class RatingDetailSerializer(RatingSerializer):
    """
    Serializer for the Rating model, Detail view
    """
    park = serializers.ReadOnlyField(source='park.id')