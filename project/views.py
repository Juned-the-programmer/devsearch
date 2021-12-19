from django.shortcuts import render

# Create your views here.
def listproject(request):
    return render(request, "project/projects.html")

def project_description(request):
    return render(request, "project/projectdisc.html")