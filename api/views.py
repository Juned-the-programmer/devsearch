from django.http import JsonResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import *
from project.models import *

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET' : 'api/projects'},
        {'GET' : 'api/projects/id'},
        {'POST' : 'api/projects/id/vote'},

        {'POST' : '/api/users/token'},
        {'POST' : '/api/users/token/refresh'}
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects , many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getproject(request,pk):
    project = Project.objects.get(pk=pk)
    serializer = ProjectSerializer(project , many=False)

    return Response(serializer.data)

@api_view(['GET'])
def getprofiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles , many=True)

    return Response(serializer.data)    