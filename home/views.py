# from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render ,redirect ,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from home.models import Project ,Task , Team ,UserProfile
from django.views.generic import TemplateView, ListView ,DetailView ,DeleteView, CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import AddForm ,TaskForm, TeamForm ,DeveloperForm
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
class ProjectDetailView( DetailView):
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
    context_object_name = 'task'

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


class TeamListView(ListView):
    model = Team
    template_name = 'team_list.html'
    context_object_name = 'teams'

class TeamDetailView(DetailView):
    model = Team
    template_name= 'team_detail.html'
    context_obj_name  = "team"

class TeamDeleteView(DeleteView):
    model=  Team
    template_name = 'team_delete.html'
    context_obj_name = "team"
    success_url = reverse_lazy("team_list")


class TeamCreateView(CreateView):
    model = Team
    template_name= 'team_form.html'
    form_class = TeamForm
    success_url = reverse_lazy("team_list")


class DeveloperListView(LoginRequiredMixin, ListView):
    model = UserProfile
    template_name = 'developer_list.html'
    context_object_name = 'developers'

def get_queryset(self):
        queryset = super().get_queryset()

        # Get the logged-in user's profile and the teams they belong to
        user_profile = self.request.user.userprofile
        user_teams = user_profile.teams.all()

        # If the user is an admin, they can see all profiles
        if self.request.user.is_staff:
            return queryset

        # Filter developers who are in the same team as the logged-in user
        queryset = queryset.filter(teams__in=user_teams).distinct()

        # Allow the user to see their own profile, even if it's private
        queryset = queryset.filter(is_private=False) | queryset.filter(is_private=True, id=user_profile.id)

        return queryset







    # def test_func(self):
    #     return self.request.user.is_superuser  # Only admin can access

    # def handle_no_permission(self):
    #     if not self.request.user.is_authenticated:
    #         return redirect('/login')  # Redirect to login if not authenticated
        
    #     # If the user is authenticated but not an admin, redirect to the no access page
    #     return redirect('no_access')

# def no_access(request):
#     return render(request, 'no_access.html')



class DeveloperDetailView(DetailView):
    model = UserProfile
    template_name = 'developer_detail.html'
    context_object_name = 'developer'

class DeveloperDeleteView(DeleteView):
    model = UserProfile
    template_name = 'developer_delete.html'
    context_object_name = 'developer'
    success_url = reverse_lazy('developer_list') 


class DeveloperCreateView(CreateView):
    model = UserProfile
    template_name = 'developer_form.html'
    form_class = DeveloperForm
    success_url = reverse_lazy('developer_list')


#superuser:admin, password:admin , email:admin@gmail.com
