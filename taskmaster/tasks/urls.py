from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView 


app_name = 'tasks'

urlpatterns = [
    # User registration page
    path('register/', views.register, name='register'),

    # Task list (homepage)
    path('', views.task_list, name='task-list'),

     # View details of a single task
    path('task/<int:pk>/', views.task_detail, name='task-detail'),

     # Create a new task
    path('task/create/', views.task_create, name='task-create'),

    # Update an existing task
    path('task/<int:pk>/update/', views.task_update, name='task-update'),

    # Delete a task
    path('task/<int:pk>/delete/', views.task_delete, name='task-delete'),

    # Logout user
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Login user using a custom login view
    path('login/', CustomLoginView.as_view(), name='login'),
]