from django import forms

from expenses.models import Expense


class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ['date', 'user']

        widgets = {
            'amount': forms.TextInput(attrs={'placeholder': 'Amount spent...'}),
            'expense_name': forms.TextInput(attrs={'placeholder': 'I spent money on...'}),
        }
