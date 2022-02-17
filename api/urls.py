from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes,name="getRoutes"),
    path('projects/',views.getProjects),
    path('projects/<str:pk>/',views.getproject),
]
