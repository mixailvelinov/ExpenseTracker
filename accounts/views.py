from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView

from accounts.forms import UserRegisterForm, UserLoginForm
from accounts.models import CustomUser


# Create your views here.

class RegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')


class UserLoginView(LoginView):
    model = CustomUser
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')
