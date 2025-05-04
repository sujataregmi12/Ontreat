from django.contrib import admin
from django.urls import path
from home import views
from home.views import IndexView, AboutView, HomePageView, PricingView, ProjectListView, ProjectDetailView, ProjectDeleteView, ProjectFormView
from home.views import TaskListView ,TaskDetailView ,TaskDeleteView ,TaskCreateView
from home.views import TeamListView ,TeamDetailView ,TeamDeleteView ,TeamCreateView
from home.views import DeveloperListView, DeveloperDetailView , DeveloperDeleteView ,DeveloperCreateView

urlpatterns = [
    path('', IndexView.as_view(), name= 'index'),
    path('about/', AboutView.as_view(), name='about'),
    path('home/', HomePageView.as_view(), name='home' ),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('project_list', ProjectListView.as_view(), name= 'project_list'),
    path('project/<int:pk>',  ProjectDetailView.as_view(), name= 'project_detail'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/add/', ProjectFormView.as_view(), name='add_project'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/addtask/', TaskCreateView.as_view(), name='add_task'),
    path('teams/', TeamListView.as_view(), name='team_list'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team_detail'),
    path('teams/<int:pk>/delete/', TeamDeleteView.as_view(), name='team_delete'),
    path('teams/create/', TeamCreateView.as_view(), name='team_create'),
    path('developers/', DeveloperListView.as_view(), name='developer_list'),
    path('developer/<int:pk>/', DeveloperDetailView.as_view(), name='developer_detail'),  
    path('developer/<int:pk>/delete/', DeveloperDeleteView.as_view(), name='developer_delete'),
    path('developer/create/', DeveloperCreateView.as_view(), name='developer_create'),

    # path('no-access/', views.no_access, name='no_access'),

]