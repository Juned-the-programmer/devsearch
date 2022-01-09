from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
@login_required(login_url='login')
def listproject(request):
    list_project = Project.objects.all()
    context = {
        'list_project': list_project
    }
    return render(request, "project/projects.html" , context)

@login_required(login_url='login')
def project_description(request,pk):
    return render(request, "project/projectdisc.html")

@login_required(login_url='login')
def add_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listproject')

    context = {
        'form' : form
    }

    return render(request , "project/addproject.html" , context)

@login_required(login_url='login')
def update_project(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST , request.FILES , instance=project)
        if form.is_valid(): 
            form.save()
            return redirect('listproject')

    context = {
        'form' : form
    }

    return render(request , "project/addproject.html" , context)

@login_required(login_url='login')
def delete_project(request,pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('listproject')

    context = {
        'object' : project
    }
    return render(request, "project/delete_object.html" , context)