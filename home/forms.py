from django import forms
from .models import Project ,User
from django.contrib.auth.models import User


class AddForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__" #['project_name', 'short_description', 'description', 'created_date', 'end_date', 'type', 'developers']
      
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']