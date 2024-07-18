from rest_framework import serializers
from .models import Profile
from bucketlist.models import Bucketlist
from ratings.models import Rating

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    ratings_count = serializers.IntegerField(read_only=True)
    bucketlist_count = serializers.IntegerField(read_only=True)
    profile_picture = serializers.ImageField(required=False)
    bucketlist = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()

    def validate_profile_picture(self, value):
        if value.size > 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 1MB!')
        if value.image.height > 2048:
            raise serializers.ValidationError(
                'Image height larger than 2048px!'
            )
        if value.image.width > 2048:
            raise serializers.ValidationError(
                'Image width larger than 2048px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def get_bucketlist(self, obj):
        bucketlist_items = Bucketlist.objects.filter(user=obj.user)
        return [
            {
                'id': item.id,
                'park': item.park.id,
                'park_name': item.park.name
            }
            for item in bucketlist_items
        ]

    def get_ratings(self, obj):
        ratings = Rating.objects.filter(user=obj.user)
        return [
            {
                'id': rating.id,
                'park': rating.park.id,
                'park_name': rating.park.name,
                'rating': rating.rating,
                'explanation': rating.explanation
            }
            for rating in ratings
        ]

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'favorite_park', 'favorite_ride', 
            'userbio', 'created_at', 'updated_at', 
            'profile_picture', 'is_owner', 'ratings_count',
            'bucketlist_count', 'bucketlist', 'ratings'
        ]