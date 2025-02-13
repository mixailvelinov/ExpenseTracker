from django import forms

from common.models import Wish


class WishCreateForm(forms.ModelForm):
    class Meta:
        model = Wish
        exclude = ['user', 'date_added', 'is_bought']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'What do you want to buy?'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price...'}),
            'image': forms.URLInput(attrs={'placeholder': 'Image URL...'})
        }

