from rest_framework import serializers
from .models import Park
from bucketlist.models import Bucketlist
from ratings.models import Rating


class ParkSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    bucketlist_id = serializers.SerializerMethodField()
    rating_id = serializers.SerializerMethodField()
    ratings_count = serializers.ReadOnlyField()
    average_rating = serializers.ReadOnlyField()
    bucketlist_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 1MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def get_bucketlist_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            bucketlist = Bucketlist.objects.filter(
                user=user, park=obj
            ).first()
            return bucketlist.id if bucketlist else None
        return None

    def get_rating_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            rating = Rating.objects.filter(
                user=user, park=obj
            ).first()
            return rating.id if rating else None
        return None

    class Meta:
        model = Park
        fields = [
            'id', 'user', 'name', 'description', 
            'image', 'street', 'city', 'postal_code',
            'country', 'opening_hours', 'entrance_fees',
            'total_number_of_rides', 
            'total_number_of_roller_coasters',
            'total_number_of_shows', 
            'total_number_of_children_rides', 'park_size',            
            'created_at', 'updated_at', 'is_owner', 'profile_id',
            'bucketlist_id', 'rating_id', 'ratings_count',
            'bucketlist_count', 'average_rating',
        ]