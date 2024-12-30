from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView

from deposits.forms import DepositCreateForm
from deposits.models import Deposit


# Create your views here.


class DepositView(CreateView):
    model = Deposit
    form_class = DepositCreateForm
    template_name = 'deposits/deposit.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user

        return super().form_valid(form)


