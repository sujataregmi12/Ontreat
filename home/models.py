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
    created_date =models.DateTimeField()
    end_date =models.DateTimeField()
    TYPE_CHOICES = [
        ('Web', 'Web Development'),
      ]
    type =models.CharField(max_length=12 ,choices=TYPE_CHOICES)
    developers = models.ManyToManyField(User, related_name='projects')
    image = models.ImageField(upload_to = 'projects/images/', null=True, blank=True )

    def __str__(self):
      return self.Project_name
    

