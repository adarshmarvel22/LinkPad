import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from posts.models import Post
from .models import Follower, Profile

from .forms import (
    RegistrationForm,
    LoginForm,
    UpdateUserForm,
    UpdateProfileForm
)

from django.shortcuts import HttpResponse

def homepage(request):
    return render(request,'profiles/homepage.html')
    
    
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created')
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'title': 'Register',
        'form': form
    }
    return render(request, 'profiles/register.html', context=context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('user_profile')
    if request.method == 'POST':
        try:
            username = request.POST['username']
            user = User.objects.filter(username=username).first()
            if user:
                password_check = user.check_password(request.POST['password'])
                if password_check:
                    user = authenticate(username=username,
                                        password=request.POST['password'])
                    login(request, user)
                    messages.success(request, 'Login Successful!')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid Password!')
            else:
                messages.error(request, 'User doesnot exist.')
                return redirect('login')
        except Exception as problem:
            messages.error(request, problem)
            return redirect('login')
    form = LoginForm()
    context = {
        'title': 'Login',
        'form': form
    }
    return render(request, 'profiles/login.html', context=context)


def current_user_view(request, user_id):
    user = User.objects.get(id=user_id)
    if user == request.user:
        return redirect('user_profile')
    context = {
        'title': user.username,
    }
    return render(request, 'profiles/current_user.html', context=context)


def current_user_posts_view(request, user_id, num_posts):
    # if request.is_ajax():
    if is_ajax(request=request):
        visible = 10
        lower = num_posts - visible
        upper = num_posts
        author = Profile.objects.filter(user__id=user_id).first()
        posts = Post.objects.filter(author=author).all()
        data = []
        for post in posts:
            item = {
                'id': post.id,
                'author': post.author.user.username,
                'user_img': post.author.image.url,
                'img': post.post_img.url,
                'liked': True if request.user in post.liked.all() else False,
                'likes': post.likes,
                'content': post.content,
                'created': post.time_diff,
                'no_of_comments': post.no_of_comments
            }
            data.append(item)
        return JsonResponse({'data': data[lower:upper], 'length': Post.objects.filter(author=author).all().count()})


def get_user_posts_view(request, num_posts):
    # if request.is_ajax():
    if is_ajax(request=request):
        visible = 10
        lower = num_posts - visible
        upper = num_posts
        posts = Post.objects.filter(author=request.user.profile).all()
        data = []
        for post in posts:
            item = {
                'id': post.id,
                'author': post.author.user.username,
                'user_img': post.author.image.url,
                'img': post.post_img.url,
                'liked': True if request.user in post.liked.all() else False,
                'likes': post.likes,
                'content': post.content,
                'created': post.time_diff,
                'no_of_comments': post.no_of_comments
            }
            data.append(item)
        return JsonResponse({'data': data[lower:upper], 'length': Post.objects.filter(author=request.user.profile).all().count()})


def user_profile_details_view(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(pk=user_id)
    profile = Profile.objects.get(pk=user.profile.pk)
    followers_list = Follower.objects.filter(user=user).all()
    details = {
        'user_id': user.id,
        'profile_id': profile.id,
        'profile_pic': profile.image.url,
        'username': user.username,
        'bio': profile.bio,
        'posts': Post.objects.filter(author=profile).all().count(),
        'followers': Follower.followers_count(user=user),
        'following': Follower.following_count(followed_by=user),
        'is_following': followers_list.filter(user=user, followed_by=request.user).exists()
    }
    return JsonResponse({'details': details})


def user_profile_view(request):
    followers = Follower.objects.filter(user=request.user).all().count()
    following = Follower.objects.filter(followed_by=request.user).all().count()
    no_posts = Post.objects.filter(author=request.user.profile).all().count()
    context = {
        'title': request.user.username,
        'following': following,
        'followers': followers,
        'no_posts': no_posts,
        'bio': request.user.profile.bio
    }
    return render(request, 'profiles/profile.html', context=context)


def edit_profile_view(request, username):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated')
            return redirect('user_profile')

    u_form = UpdateUserForm(instance=request.user)
    p_form = UpdateProfileForm(instance=request.user.profile)
    context = {
        'title': 'Edit Profile',
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profiles/edit_profile.html', context=context)


def get_search_users_view(request):
    print(type(request))
    # if request.is_ajax():
    if is_ajax(request=request):
        username = request.GET['username']
        users = User.objects.filter(username__icontains=username)
        data = []
        for user in users:
            item = {
                'id': user.id,
                'username': user.username,
                'profile_pic': user.profile.image.url
            }
            data.append(item)
    return JsonResponse({'data': data[:10]})


def follow_unfollow_view(request):
    user = User.objects.get(pk=request.POST['user_id'])
    followers_list = Follower.objects.filter(user=user).all()
    is_following = followers_list.filter(user=user, followed_by=request.user)
    if(is_following.exists()):
        is_following.delete()
        followers = Follower.objects.filter(user=user).all().count()
        return JsonResponse({'follow': False, 'followers': followers})
    else:
        Follower.objects.create(user=user, followed_by=request.user)
        followers = Follower.objects.filter(user=user).all().count()
        return JsonResponse({'follow': True, 'followers': followers})


def search_view(request):
    return render(request, 'profiles/search.html', context={'title': 'Search'})


def following(request):
    return render(request, 'profiles/following.html', context={'title': 'Following'})


@ login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('login')


from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Profile, Follower
from django.contrib import messages
from .forms import UpdateUserForm, UpdateProfileForm
from django.views.decorators.csrf import csrf_exempt

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def get_search_users_view(request):
    if is_ajax(request=request):
        username = request.GET.get('username', '')
        users = User.objects.filter(username__icontains=username)
        data = []
        for user in users:
            is_following = Follower.is_following(user, request.user)
            item = {
                'id': user.id,
                'username': user.username,
                'profile_pic': user.profile.image.url,
                'is_following': is_following
            }
            data.append(item)
        return JsonResponse({'data': data[:10]})
    return JsonResponse({'data': []})

@csrf_exempt
def follow_unfollow_view(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.POST['user_id'])
        is_following = Follower.is_following(user, request.user)
        if is_following:
            Follower.objects.filter(user=user, followed_by=request.user).delete()
            follow_status = False
        else:
            Follower.objects.create(user=user, followed_by=request.user)
            follow_status = True
        followers_count = Follower.followers_count(user)
        return JsonResponse({'follow': follow_status, 'followers': followers_count})

def search_view(request):
    return render(request, 'profiles/search.html', context={'title': 'Search'})

def chat(request):
    return render(request, 'profiles/chat.html')