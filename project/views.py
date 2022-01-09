from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
@login_required(login_url='login')
def listproject(request):
    return render(request, "project/projects.html")

@login_required(login_url='login')
def project_description(request):
    return render(request, "project/projectdisc.html")

@login_required(login_url='login')
def add_project(request):
    project_form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm()
        if form.is_valid():
            form.save()

    context = {
        'project_form' : project_form
    }

    return render(request , "project/addproject.html" , context)