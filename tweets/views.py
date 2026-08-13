from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Tweet
from utils import persian_timesince


def add_persian_time_to_tweet(tweet):
    tweet.fa_time = persian_timesince(tweet.created_at)
    for reply in tweet.replies.all():
        add_persian_time_to_tweet(reply)


@login_required
def home_view(request):
    if request.method == "POST":
        content = request.POST.get("content")
        parent_id = request.POST.get("parent")
        if content:
            parent = None
            if parent_id:
                parent = get_object_or_404(Tweet, id=parent_id)
            Tweet.objects.create(author=request.user, content=content, parent=parent)
        return redirect("home")

    following_users = request.user.profile.following.all()
    tweets = Tweet.objects.filter(author__in=following_users).order_by("-created_at")
    own_tweets = Tweet.objects.filter(author=request.user)
    tweets = (tweets | own_tweets).distinct().order_by("-created_at")

    for tweet in tweets:
        tweet.fa_time = persian_timesince(tweet.created_at)

    return render(request, "home.html", {"tweets": tweets})


@login_required
def tweet_detail_view(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    top_replies = Tweet.objects.filter(parent=tweet).order_by("created_at")

    tweet.fa_time = persian_timesince(tweet.created_at)

    def process_replies(replies):
        for reply in replies:
            reply.fa_time = persian_timesince(reply.created_at)
            if reply.replies.exists():
                process_replies(reply.replies.all())

    process_replies(top_replies)

    context = {
        "tweet": tweet,
        "top_replies": top_replies,
    }
    return render(request, "tweet_detail.html", context)


@login_required
def like_tweet_view(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.user in tweet.likes.all():
        tweet.likes.remove(request.user)
        status = "unliked"
    else:
        tweet.likes.add(request.user)
        status = "liked"

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({"status": status, "count": tweet.likes.count()})
    return redirect("home")


@login_required
def follow_view(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    if request.user != user_to_follow:
        if request.user.profile.following.filter(id=user_to_follow.id).exists():
            request.user.profile.following.remove(user_to_follow)
        else:
            request.user.profile.following.add(user_to_follow)
    return redirect("profile", username=username)


@login_required
def create_tweet_view(request):
    if request.method == "POST":
        content = request.POST.get("content")
        parent_id = request.POST.get("parent")

        if content:
            parent = None
            if parent_id:
                parent = get_object_or_404(Tweet, id=parent_id)

            tweet = Tweet.objects.create(
                author=request.user, content=content, parent=parent
            )

            return redirect("tweet_detail", tweet_id=tweet.id)

    return redirect("home")
