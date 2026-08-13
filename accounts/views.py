from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserEditForm, ProfileEditForm
from django.contrib.auth.models import User
from tweets.models import Tweet


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def edit_profile_view(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "پروفایل با موفقیت ویرایش شد.")
            return redirect("profile", username=request.user.username)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        "edit_profile.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "form": profile_form,
        },
    )


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    user_tweets = Tweet.objects.filter(author=user).order_by("-created_at")

    is_following = False
    if request.user.is_authenticated:
        is_following = request.user.profile.following.filter(id=user.id).exists()

    context = {
        "profile_user": user,
        "user_tweets": user_tweets,
        "tweets_count": user_tweets.count(),
        "following_count": user.profile.following.count(),
        "followers_count": user.followers.count(),
        "is_following": is_following,
    }
    return render(request, "profile.html", context)
