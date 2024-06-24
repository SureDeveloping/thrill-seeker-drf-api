from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    ratings_count = serializers.ReadOnlyField()
    bucketlist_count = serializers.ReadOnlyField()
    like_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user


    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'favorite_park', 'favorite_ride', 
            'userbio', 'created_at', 'updated_at', 
            'profile_picture', 'is_owner', 'ratings_count',
            'bucketlist_count', 'like_count',
        ]
