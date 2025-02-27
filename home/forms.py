from django import forms
from .models import Project ,User
from django.contrib.auth.models import User
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput



class AddForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__" #['project_name', 'short_description', 'description', 'created_date', 'end_date', 'type', 'developers','datepicker']
        widgets = {
            "created_date": DatePickerInput(),
            "end_date": DatePickerInput(),
        }
      

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

#imagefield:
class Project(forms.ModelForm):
   image = forms.ImageField(
       label= "photo",
       widget = forms.ClearableFileInput(attrs={
           'class':'form-control'
       })
      
) 
