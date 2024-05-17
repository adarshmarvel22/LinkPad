from django.urls import path
from . import views

app_name = 'features'

urlpatterns = [
    # Club URLs
    path('', views.home, name='home'),
    path('recommend', views.recommend, name='recommend'),

    path('club_list/', views.club_list, name='club_list'),
    path('club_detail/<int:pk>/', views.club_detail, name='club_detail'),
    path('club_create/create/', views.club_create, name='club_create'),
    path('club_update/<int:pk>/update/', views.club_update, name='club_update'),
    path('club_delete/<int:pk>/delete/', views.club_delete, name='club_delete'),

    # Hall of Fame URLs
    path('hall_of_fame_list/', views.hall_of_fame_list, name='hall_of_fame_list'),
    path('hall_of_fame_detail/<int:pk>/', views.hall_of_fame_detail, name='hall_of_fame_detail'),
    path('hall_of_fame_create/create/', views.hall_of_fame_create, name='hall_of_fame_create'),
    path('hall_of_fame_update/<int:pk>/update/', views.hall_of_fame_update, name='hall_of_fame_update'),
    path('hall_of_fame_delete/<int:pk>/delete/', views.hall_of_fame_delete, name='hall_of_fame_delete'),

    # Event URLs
    path('event_list/', views.event_list, name='event_list'),
    path('event_detail/<int:pk>/', views.event_detail, name='event_detail'),
    path('event_create/create/', views.event_create, name='event_create'),
    path('event_update/<int:pk>/update/', views.event_update, name='event_update'),
    path('event_delete/<int:pk>/delete/', views.event_delete, name='event_delete'),

    # Resources URLs
    path('resources_list/', views.resources_list, name='resources_list'),
    path('resources_detail/<int:pk>/', views.resources_detail, name='resources_detail'),
    path('resources_create/create/', views.resources_create, name='resources_create'),
    path('resources_update/<int:pk>/update/', views.resources_update, name='resources_update'),
    path('resources_delete/<int:pk>/delete/', views.resources_delete, name='resources_delete'),
    

        # Jobs URLs
    path('job_list/', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('jobs/create/', views.job_create, name='job_create'),
    path('jobs/<int:pk>/update/', views.job_update, name='job_update'),
    path('jobs/<int:pk>/delete/', views.job_delete, name='job_delete'),
]
