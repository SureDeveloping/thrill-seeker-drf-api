from rest_framework import serializers
from .models import Park


class ParkSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='author.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')

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
        ]
