from django.shortcuts import render ,redirect
from django.http import HttpResponse
from home.models import Project
from django.contrib.auth.models import User
from datetime import datetime
from django.views.generic import TemplateView, ListView, DetailView, DeleteView 
from django.urls import reverse_lazy

# Create your views here.

### Use Class Based View
# https://docs.djangoproject.com/en/5.1/topics/class-based-views/
###

class IndexView(TemplateView):
    template_name = "index.html"


#### Modifiy the projectlist template as you prefer.
class ProjectListView(ListView):
    template_name = "projectlist.html"
    model = Project
    context_object_name = "project_list"

#### Create a ProjectDetailView, ProjectDeleteView
#projectDetailview.
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projectdetail.html'
    context_object_name = 'project_detail'

#projectDeleteview
class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'  # The template that will ask for confirmation
    context_object_name = 'project_delete'
    success_url = reverse_lazy('project_list')





def index(request):
        if request.method =='POST':
            name = request.POST.get('name')
            short_description = request.POST.get('short_description')
            description = request.POST.get('description')
            created_date = request.POST.get('created_date')
            end_date = request.POST.get('end_date')
            type = request.POST.get('type')
            developer_ids = request.POST.getlist('developers')

            project= Project(name=name, short_description=short_description,description=description,
                          created_date=created_date,end_date=end_date,type=type)
            for developer_id in developer_ids:
                developer = User.objects.get(id=developer_id)  # Get the developer by ID
                Project.developers.add(developer)
            project.save()
        return render(request, 'index.html')
     