from django import forms
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from datetime import datetime


class TaskForm(forms.Form):
    project = forms.IntegerField()
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
    content = forms.CharField(required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if type(start_time) is not datetime or type(end_time) is not datetime:
            pass  # Django does this validation for DateTimeField
        elif start_time > end_time:
            raise ValidationError(
                _('end_time must be later than start_time: start_time=%(start_time)s, end_time=%(end_time)s'),
                code='invalid time',
                params={'start_time': start_time,
                        'end_time': end_time},
            )
