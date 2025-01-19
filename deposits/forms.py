from django import forms

from deposits.models import Deposit


class DepositCreateForm(forms.ModelForm):
    class Meta:
        model = Deposit
        exclude = ['date', 'user']

        widgets = {
            'amount': forms.TextInput(attrs={'placeholder': 'What amount are you depositing?'}),
            'description': forms.TextInput(attrs={'placeholder': 'I got the funds from...'}),
        }



