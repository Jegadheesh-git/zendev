from django import forms
from .models import Competition

class CompetitionForm(forms.ModelForm):
    class Meta:
        exclude = ['createdBy']
        model = Competition