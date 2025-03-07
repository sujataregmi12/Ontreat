from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Signup(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)  

    def __str__(self):
        return self.username


ROLE_CHOICES = [
        ('developer', 'Developer'),
        ('project_lead', 'Project Lead'),
        ('project_manager', 'Project Manager'),
    ]
   
class UserProfile(models.Model):
    display_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=150, choices=ROLE_CHOICES, null=True, blank=True)
    about_me =models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to = 'projects/images/',blank=True, null=True) 
    
    def __str__(self):
        if self.display_name:
            return self.display_name
        else:
            f"User_{self.id}"
 
class Project(models.Model):
    Project_name= models.CharField(max_length=122)
    short_description = models.CharField(max_length=122)
    description = models.TextField(max_length=122)
    created_date =models.DateTimeField(null=True, blank=True)
    end_date =models.DateTimeField(null=True, blank=True)
    TYPE_CHOICES = [
        ('Web', 'Web Development'),
      ]
    type =models.CharField(max_length=12 ,choices=TYPE_CHOICES)
    developers = models.ManyToManyField(UserProfile, related_name='projects', null=True, blank=True)
    image = models.ImageField(upload_to = 'projects/images/', null=True, blank=True )

    def __str__(self):
      return self.Project_name
    
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    project_lead = models.ForeignKey(UserProfile, related_name='lead_of_teams', on_delete=models.SET_NULL, null=True, blank=True)
    developers = models.ManyToManyField(UserProfile, related_name='teams', blank=True)
    projects = models.ManyToManyField(Project, related_name='teams_assigned', blank=True)
    

    def __str__(self):
        return self.name


class Task(models.Model):
    title=models.CharField(max_length=150)
    description= models.TextField(max_length=250)
    assigned_to_team = models.ForeignKey(Team, related_name='tasks_assigned_to_team', null=True, blank=True, on_delete=models.SET_NULL)

  
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    priority=models.CharField(max_length=150,choices=PRIORITY_CHOICES)
   
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('blocked', 'Blocked'),
        ('on_hold', 'On Hold'),
    ]
    status=models.CharField(max_length=150, choices=STATUS_CHOICES)
    deadline=models.DateTimeField(null=True, blank=True)
    created_date =models.DateTimeField(null=True, blank=True)
    end_date =models.DateTimeField(null=True, blank=True)

    def __str__(self):
      return self.title
    

#username and password of superuser: admin, email:admin@gmail.com