from django.contrib import admin
from home.models import Project ,Task, Team, Developer
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Team)
admin.site.register(Developer)
