from django import forms
from .models import Money

class MoneyForm(forms.ModelForm):
    class Meta:
        model = Money
        fields = ['purpose', 'name', 'amount', ]