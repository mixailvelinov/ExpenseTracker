from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView

from deposits.forms import DepositCreateForm
from deposits.models import Deposit


# Create your views here.


class DepositView(CreateView):
    model = Deposit
    form_class = DepositCreateForm
    template_name = 'deposits/deposit.html'
    success_url = reverse_lazy('deposit')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_funds'] = self.request.user.balance

        return context


class DepositHistory(ListView):
    model = Deposit
    template_name = 'deposits/deposit-history.html'

    def get_queryset(self):
        queryset = Deposit.objects.filter(user_id=self.request.user.id).order_by('-date')

        return queryset
