from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'favorite_park', 'favorite_ride', 
            'userbio', 'created_at', 'updated_at', 
            'profile_picture'
        ]
