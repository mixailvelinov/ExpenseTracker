from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView

from accounts.forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from accounts.models import CustomUser, Profile


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


class UserLogoutView(LogoutView):
    pass


class UserDetailsView(ListView):
    model = CustomUser
    template_name = 'accounts/details.html'


class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = 'accounts/edit.html'
    form_class = UserUpdateForm
    success_url = 'index'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'id': self.object.id})

    #make functionality to make sure that the user can change only his details and not someone else's


def user_delete_view(request, id):
    user = CustomUser.objects.filter(id=id)

    context = {
        'user': user,
    }

    if request.method == 'POST':
        user.delete()
        return redirect('index')

    return render(request, 'accounts/delete.html', context)
