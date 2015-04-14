from django import forms

forms.DateInput.input_type = "date"


class DatepickerForm(forms.Form):
    """
    Datepicker for selecting posts from day
    """
    dateselector = forms.DateField(label='Pick a date')