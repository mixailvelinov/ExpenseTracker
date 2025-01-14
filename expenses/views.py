from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView
from expenses.forms import ExpenseCreateForm
from expenses.models import Expense


# Create your views here.

class ExpensesView(CreateView):
    model = Expense
    form_class = ExpenseCreateForm
    template_name = 'expenses/expenses.html'
    success_url = reverse_lazy('expenses')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_funds'] = self.request.user.balance

        return context


class ExpensesHistory(ListView):
    model = Expense
    template_name = 'expenses/expenses-history.html'

    def get_queryset(self):
        queryset = Expense.objects.filter(user_id=self.request.user.id).order_by('-date')

        return queryset