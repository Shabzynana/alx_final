from django import forms
from .models import Task
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.forms.widgets import DateInput


class TaskForm(forms.ModelForm):
    # date_created = forms.DateField()
    class Meta:
        model = Task
        fields = ['title','content','start_date','end_date']
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),

        }
        # widgets = {
        #     'date_created': DatePickerInput(),
        # }
