from django.urls import path
from . import views

urlpatterns = [
    path('projects/',views.listproject,name="listproject"),
    path('project-description/<str:pk>/',views.project_description,name="project-description"),
    path('addproject/',views.add_project,name="addproject"),
    path('update_project/<str:pk>/',views.update_project,name="update_project"),
    path('delete_project/<str:pk>/',views.delete_project,name="delete_project"),
]
