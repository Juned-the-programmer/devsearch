from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.db.models import Q
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage

# Create your views here.
@login_required(login_url='login')
def listproject(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    list_project = Project.objects.distinct().filter(
        Q(title__icontains=search_query) | 
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )

    page = request.GET.get('page')
    result = 10
    paginator = Paginator(list_project, result)

    try:
        list_project = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        list_project = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        list_project = paginator.page(page)

    leftIndex = (int(page) -4)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) +5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex , rightIndex)

    context = {
        'list_project': list_project ,
        'search_query': search_query ,
        'paginator' : paginator ,
        'custom_range': custom_range ,
    }
    return render(request, "project/projects.html" , context)

@login_required(login_url='login')
def project_description(request,pk):
    project = Project.objects.get(id=pk)
    context = {
        'project': project
    }
    return render(request, "project/projectdisc.html" , context)

@login_required(login_url='login')
def add_project(request):
    user = request.user.username
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = user
            project.save()
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