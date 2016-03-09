# from forms import ProjectModelForm
from .models import Project
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect


def project_list(request):
    return render(request, 'projects/project_list.html')