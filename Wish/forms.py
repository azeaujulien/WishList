from django import forms
from django.forms import modelformset_factory

from Wish.models import Wish

WishCreateFormSet = modelformset_factory(
    Wish, fields=['name', 'description'], extra=1
)


class WishCreateForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['name', 'description']
