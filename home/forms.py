from django import forms
from .models import Project
from django.contrib.auth.models import User

class AddForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__" #['name', 'short_description', 'description', 'created_date', 'end_date', 'type', 'developers']