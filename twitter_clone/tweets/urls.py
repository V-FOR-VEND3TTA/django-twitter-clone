from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Display feed of tweets
    path('tweet/<int:id>/', views.tweet_detail, name='tweet_detail'),
    path('tweet/new/', views.create_tweet, name='create_tweet'),
]