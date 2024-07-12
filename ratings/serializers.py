from rest_framework import serializers
from django.db import IntegrityError
from .models import Rating
from likes.models import Like
from django.contrib.humanize.templatetags.humanize import naturaltime


class RatingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Rating model
    """
    user = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_picture = serializers.ReadOnlyField(
        source='user.profile.profile_picture.url')
    like_id = serializers.SerializerMethodField()
    created_at =serializers.SerializerMethodField()
    updated_at =serializers.SerializerMethodField()
    explanation = serializers.CharField(allow_blank=False)
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                user=user, rating=obj
            ).first()
            return like.id if like else None
        return None


    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You have already rated this park.'
            })

    class Meta:
        model = Rating
        fields = [
            'id', 'user', 'is_owner', 'park', 'rating', 
            'last_visisted_at','explanation', 
            'profile_id', 'profile_picture',
            'created_at', 'updated_at', 'like_id',]

class RatingDetailSerializer(RatingSerializer):
    """
    Serializer for the Rating model, Detail view
    """
    park = serializers.ReadOnlyField(source='park.id')