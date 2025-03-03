from django.shortcuts import render ,redirect
from django.http import HttpResponse
from home.models import Project ,Task
from django.views.generic import TemplateView, ListView ,DetailView ,DeleteView, CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import AddForm ,TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
# https://docs.djangoproject.com/en/5.1/topics/class-based-views/

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    login_url = '/account/login'  # Specify where to redirect users who aren't logged in

#### Modifiy the projectlist template as you prefer.
class ProjectListView(ListView):
    template_name = "projectlist.html"
    model = Project
    context_object_name = "project_list"

#### Create a ProjectDetailView, ProjectDeleteView
#ProjectDetailView
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'  # The template you want to use
    context_object_name = 'project'

#projectDeleteView
class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_delete.html'  # Template for the confirmation page
    context_object_name = 'project'  # The name of the object in the template context
    success_url = reverse_lazy('project_list') 

# To Create a object in any table you have to use CreateView
# To use FormView you have to call method form_valid which is used for form validation where you have to call save function
# https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-editing/

class ProjectFormView(CreateView):
    model = Project
    template_name = 'project_form.html'  # Template for the confirmation page
    form_class= AddForm  # The name of the object in the template context
    success_url = reverse_lazy('project_list') 


class TaskListView(ListView):
    model= Task
    template_name ='task_list.html'
    context_object_name = "task_list"

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = "task_detail"

class TaskDeleteView(DeleteView):
    model= Task
    template_name = 'task_delete.html'
    context_object_name = "task_delete"
    success_url = reverse_lazy('task_list') 


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'taskform.html'
    success_url = reverse_lazy('task_list') 



#superuser:admin, password:admin , email:admin@gmail.com
