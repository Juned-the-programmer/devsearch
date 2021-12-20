from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def listproject(request):
    return render(request, "project/projects.html")

@login_required(login_url='login')
def project_description(request):
    return render(request, "project/projectdisc.html")

@login_required(login_url='login')
def addproject(request):
    return redirect(request , "project/addproject.html")