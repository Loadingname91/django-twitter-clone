from django.urls import path
from .views import CreateTweetView, ListTweetsView, LikeTweetView

urlpatterns = [
    path('create/', CreateTweetView.as_view(), name='create_tweet'),
    path('', ListTweetsView.as_view(), name='list_tweets'),
   path('like/<int:tweet_id>/', LikeTweetView.as_view(), name='like_tweet'),
]