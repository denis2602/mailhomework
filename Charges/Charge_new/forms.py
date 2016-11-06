from django import forms
import datetime
from django.core.exceptions import ValidationError


class ChargesForm(forms.Form):

    value = forms.DecimalField(label='Сумма', required=True)
    date = forms.DateField(label='Дата', required=True)

    def clean(self):
        value = self.cleaned_data.get('value')
        date = self.cleaned_data.get('date')
        if (value < 0) and (date > date.today()):
            self.add_error('date', 'Неправильная дата')
