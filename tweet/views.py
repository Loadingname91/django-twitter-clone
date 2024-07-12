
from rest_framework import generics, permissions
from .models import Tweet, Like
from .serializers import TweetSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Count, Exists, OuterRef
from django.db import transaction
from rest_framework.views import APIView

class CreateTweetView(generics.CreateAPIView):
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Create a mutable copy of the request data
        data = request.data.copy()
        
        # Add the user to the data
        data['user'] = request.user.id
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListTweetsView(generics.ListAPIView):
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tweet.objects.annotate(
            likes_count=Count('like'),
            is_liked=Exists(Like.objects.filter(user=user, tweet=OuterRef('pk')))
        ).order_by('-created_at')

class LikeTweetView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ['POST']

    @transaction.atomic
    def post(self, request, tweet_id):
        tweet = get_object_or_404(Tweet, id=tweet_id)
        like, created = Like.objects.get_or_create(user=request.user, tweet=tweet)
        
        if not created:
            like.delete()
            action = 'unliked'
        else:
            action = 'liked'

        likes_count = Like.objects.filter(tweet=tweet).count()

        return Response({
            'action': action,
            'tweet': {
                'id': tweet.id,
                'user': tweet.user.username,
                'content': tweet.content,
                'created_at': tweet.created_at,
                'likes_count': likes_count,
                'is_liked': action == 'liked'
            }
        }, status=status.HTTP_200_OK)