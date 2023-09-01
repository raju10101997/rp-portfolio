import imp
# from django.conf import settings
from personal_portfolio import settings
from django.shortcuts import render
from projects.models import Project
# Create your views here.


def project_index(request):
    projects = Project.objects.all()
    print(projects, "AAAAAAAAAAAAAAAAAAAAAAAAAAa")
    context = {
        "projects": projects
    }
    print(settings.BASE_DIR)
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "project_detail.html", context)
