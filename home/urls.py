from django.contrib import admin
from django.urls import path
from home import views
from home.views import IndexView, ProjectListView, ProjectDetailView, ProjectDeleteView, ProjectFormView

urlpatterns = [
    path('', IndexView.as_view(), name= 'index'),
    path('register/', views.register, name='register'),
    path("login", views.loginUser, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path('project_list', ProjectListView.as_view(), name= 'project_list'),
    path('project/<int:pk>',  ProjectDetailView.as_view(), name= 'project_detail'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/add/', ProjectFormView.as_view(), name='add_project'),
    
]
