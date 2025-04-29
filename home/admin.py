from django.contrib import admin
from home.models import Project ,Task, Team, UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["display_name", "user", "role", "is_active"]

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Team)
admin.site.register(UserProfile, UserProfileAdmin)
