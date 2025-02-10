from django.shortcuts import render ,redirect
from django.http import HttpResponse
from home.models import Project
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.
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
     