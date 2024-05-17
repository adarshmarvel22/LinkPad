from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *



urlpatterns = [
    path('homepage/', homepage , name='homepage'),
    path('chat/', chat , name='chat'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
  path('search/', search_view, name='search'),
    path('search-users/', get_search_users_view, name='search_users'),
    path('follow-unfollow/', follow_unfollow_view, name='follow_unfollow'),
    path('u/profile-details/<int:user_id>/', user_profile_details_view,
         name='user_profile_details'),
    path('u/profile/<int:user_id>/', current_user_view,
         name='current_user_profile'),
    path('u/<int:user_id>/<int:num_posts>/',
         current_user_posts_view, name='current_user_posts'),
    path('u/profile', user_profile_view, name='user_profile'),
    path('u/follow-unfollw/', follow_unfollow_view, name='follow_unfollow'),
    path('u/<username>/edit-profile/', edit_profile_view, name='edit_profile'),
    path('u/get-user-posts/<int:num_posts>/',
         get_user_posts_view, name='get_user_posts'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="profiles/reset_request.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="profiles/reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name="profiles/reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="profiles/reset_complete.html"), name='password_reset_complete')
]
