from django.shortcuts import render ,redirect
from django.http import HttpResponse
from home.models import Project 
from .forms import SignupForm
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from django.views.generic import TemplateView, ListView ,DetailView ,DeleteView, CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import AddForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# https://docs.djangoproject.com/en/5.1/topics/class-based-views/

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    login_url = '/login'  # Specify where to redirect users who aren't logged in

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
   


# views.py
def register(request):
 form = SignupForm(request.POST)
 if form.is_valid():
            # Process the form data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Create the user and save
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            messages.success(request, 'Your account has been created successfully!')
            return redirect('/login')  # Redirect to login page
 else:
        form = SignupForm()  # Initialize the form for GET request
    
 return render(request, 'register.html', {'form': form})


def index(request): 
  if request.method =='POST':
    project_name = request.POST.get('Project_name')
    short_description = request.POST.get('short_description')
    description = request.POST.get('description')
    created_date = request.POST.get('created_date')
    end_date = request.POST.get('end_date')
    type = request.POST.get('type')
    developer_ids = request.POST.getlist('developers')

    project= Project(project_name=project_name, short_description=short_description,description=description,
        created_date=created_date,end_date=end_date,type=type)
    for developer_id in developer_ids:
        developer = User.objects.get(id=developer_id)  # Get the developer by ID
        Project.developers.add(developer)
    project.save()
    return render(request, "login.html")


def loginUser(request):
    if request.method=="POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        # A backend authenticated the credentials
            return redirect("/")       
     
        else:
         # No backend authenticated the credentials
            return render(request, "login.html")
    
        #check f user has entered correct credentials
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")
            
#superuser:sujataregmi, password:sujataregmi ,email:sujataregmi@gmail.com
