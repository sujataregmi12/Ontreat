from django import forms
from .models import Project ,User ,Task ,Team ,UserProfile ,LogBook
from django.contrib.auth.models import User
from bootstrap_datepicker_plus.widgets import DatePickerInput



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

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__" #['Title', 'Description', 'priority', 'status', 'Deadline']
        widgets = {
            "created_date": DatePickerInput(),
            "end_date": DatePickerInput(),
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),

        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__" 

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields= "__all__"


class Developer(forms.ModelForm):
   image = forms.ImageField(
       label= "photo",
       widget = forms.ClearableFileInput(attrs={
           'class':'form-control'
       })
   )


class LogBookForm(forms.ModelForm):
    class Meta:
        model = LogBook
        fields = ['tasks_done', 'tasks_remaining']
        widgets = {
            'tasks_done': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Describe completed tasks...'}),
            'tasks_remaining': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Describe remaining tasks...'}),
        }
