"""Define URL patterns for users."""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = "users"

urlpatterns = [
    # Login 
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    
    # Logout
    path('logout/', views.logout_view, name='logout'),
    
    # Register
    path('register/', views.register, name='register'),
]
