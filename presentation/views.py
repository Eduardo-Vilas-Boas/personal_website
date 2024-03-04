from django.shortcuts import HttpResponse, render

from .models import ProjectItem


# Create your views here.
def home(request):
    return render(request, "home.html")


def projects(request):
    items = ProjectItem.objects.all()
    return render(request, "projects.html", {"projects": items})
