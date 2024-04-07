from django import forms
from accounts.models import Account


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    recipients = forms.ModelMultipleChoiceField(
        queryset=Account.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )
