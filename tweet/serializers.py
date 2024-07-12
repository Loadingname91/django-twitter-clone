from rest_framework import serializers
from .models import Tweet, Like



class TweetSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    likes_count = serializers.IntegerField(read_only=True)
    is_liked = serializers.BooleanField(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'user', 'content', 'created_at', 'likes_count', 'is_liked']