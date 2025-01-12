from django import forms

from common.models import Wish


class WishCreateForm(forms.ModelForm):
    class Meta:
        model = Wish
        exclude = ['user', 'date_added', 'is_bought']

