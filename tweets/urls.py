from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("tweet/<int:tweet_id>/", views.tweet_detail_view, name="tweet_detail"),
    path("like/<int:tweet_id>/", views.like_tweet_view, name="like_tweet"),
    path("follow/<str:username>/", views.follow_view, name="follow"),
    path("create/", views.create_tweet_view, name="create_tweet"),
]
