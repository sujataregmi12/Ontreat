from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
   
    name= models.CharField(max_length=122)
    short_description = models.CharField(max_length=122)
    description = models.TextField(max_length=122)
    created_date =models.DateTimeField()
    end_date =models.DateTimeField()
    TYPE_CHOICES = [
        ('Web', 'Web Development'),
      ]
    type =models.CharField(max_length=12 ,choices=TYPE_CHOICES)
    developers = models.ManyToManyField(User, related_name='projects')

def __str__(self):
        return self.name