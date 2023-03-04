from django.shortcuts import render
from .models import Project, Tag

# Create your views here.

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'project/projects.html', context)

def project(request, id):
    project = Project.objects.get(id=id)
    tags = Tag.objects.all()
    context = {
        'project':project,
        'tags':tags
    }
    return render(request, 'project/project.html', context)
