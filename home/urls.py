from django.contrib import admin
from django.urls import path
from home import views
from home.views import IndexView, ProjectListView,ProjectDetailView ,ProjectDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name= 'index'),
    path('project_list', ProjectListView.as_view(), name= 'project_list'),
    path('<int:pk>', ProjectDetailView.as_view(), name= 'detail'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name= 'delete'),
    
]
