from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
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


def user_details(request, id):
    user = get_object_or_404(CustomUser, id=id)

    if user != request.user:
        raise PermissionDenied("You can't view this account!")

    context = {
        'user': user,
    }

    return render(request, 'accounts/details.html', context)


class UserUpdateView(UpdateView, LoginRequiredMixin):
    model = CustomUser
    template_name = 'accounts/edit.html'
    form_class = UserUpdateForm
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'id': self.object.id})

    def get_object(self, queryset=None):
        user = CustomUser.objects.get(pk=self.kwargs['id'])

        if user != self.request.user:
            raise PermissionDenied('You do not have permission to edit this account!')

        return user


def user_delete_view(request, id):
    user = get_object_or_404(CustomUser, id=id)

    context = {
        'user': user,
    }

    if user != request.user:
        raise PermissionDenied("You can't delete someone else's account!")

    if request.method == 'POST':
        user.delete()
        return redirect('index')

    return render(request, 'accounts/delete.html', context)

