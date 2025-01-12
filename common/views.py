from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy


from accounts.models import Profile
from common.forms import WishCreateForm
from common.models import Wish


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            profile = None
    else:
        user = None
        profile = None

    context = {'user': user}

    return render(request, 'common/index.html', context)


class WishCreate(CreateView, LoginRequiredMixin):
    model = Wish
    form_class = WishCreateForm
    template_name = 'common/wish-create.html'
    success_url = reverse_lazy('wishlist')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)


class WishlistView(ListView, LoginRequiredMixin):
    model = Wish
    template_name = 'common/wishlist.html'

    def get_queryset(self):
        queryset = Wish.objects.filter(user_id=self.request.user.id)
        return queryset


class WishEdit(UpdateView, LoginRequiredMixin):
    model = Wish
    form_class = WishCreateForm
    template_name = 'common/wish-create.html'
    success_url = reverse_lazy('wishlist')
    pk_url_kwarg = 'id'


class WishDelete(DeleteView, LoginRequiredMixin):
    model = Wish
    success_url = reverse_lazy('wishlist')
    pk_url_kwarg = 'id'
