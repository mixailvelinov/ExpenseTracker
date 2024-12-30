from django import forms

from deposits.models import Deposit


class DepositCreateForm(forms.ModelForm):
    class Meta:
        model = Deposit
        exclude = ['date', 'user']

