from django.urls import path
from .views import LoginView, LogoutView  # Import the correct classes

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
