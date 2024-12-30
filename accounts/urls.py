from django.urls import path
from accounts.views import UserLoginView, RegisterView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]