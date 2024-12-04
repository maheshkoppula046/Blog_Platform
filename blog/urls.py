from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('add/', views.add_post, name='add_post'),  # Add this line for adding a new post
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),  # Add this line for editing a post
]


