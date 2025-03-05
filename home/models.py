from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Signup(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)  

    def __str__(self):
        return self.username

 
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
    developers = models.ManyToManyField(User, related_name='projects')
    image = models.ImageField(upload_to = 'projects/images/', null=True, blank=True )

    def __str__(self):
      return self.Project_name

  
    
class Developer(models.Model):
    name = models.CharField(max_length=50)
        
    def __str__(self):
        return self.name
    
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    project_lead = models.ForeignKey(Developer, related_name='lead_of_teams', on_delete=models.SET_NULL, null=True, blank=True)
    developers = models.ManyToManyField(Developer, related_name='teams', blank=True)
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