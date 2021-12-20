from django.urls import path
from . import views

urlpatterns = [
    path('projects/',views.listproject,name="listproject"),
    path('project-description/',views.project_description,name="project-description"),
    path('addproject/',views.addproject,name="addproject"),
]
