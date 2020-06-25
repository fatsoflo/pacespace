from django.db import models
from django.shortcuts import render, redirect
from database.models import SchoolClass, Project, PaceUser
from database.user_functions import *
from .forms import CreateProjectForm, SubmitProjectForm

STATUS_CHOICES = [
    ('A', 'Assigned'),
    ('S', 'Submitted'),
    ('O', 'Overdue'),
    ('SL', 'Submitted Late')
]    

status = models.CharField(
    max_length=2,
    choices=STATUS_CHOICES,
    default="A"
)

def all_project(request, pk):
    if request.user.is_authenticated:
        # user = request.user
        return render(request, "all_project.html")
    else:
        return redirect('index')

def view_project(request, pk):
    if request.user.is_authenticated:
        # user = request.user
        # if in user.schoolclass
        project = Project.objects.get(pk=pk)
        context = {
            'project':project,
        }
        return render(request, "view_project.html", context=context)
    else:
        return redirect('index')    
