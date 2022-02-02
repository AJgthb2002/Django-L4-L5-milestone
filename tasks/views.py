# Add all your views here
from operator import index
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from tasks.models import Task


def tasks_view(request):
    search_term=request.GET.get('search')
    tasks_list= Task.objects.filter(deleted=False).filter(completed=False)
    if search_term:
        tasks_list= tasks_list.filter(title__icontains=search_term)
    return render(request, "tasks.html", {"tasks":tasks_list})

def add_task_view(request):
    task_value= request.GET.get("task")
    task_obj= Task(title=task_value)
    task_obj.save()
    return HttpResponseRedirect("/tasks")

def delete_task_view(request, index):
    Task.objects.filter(id=index).update(deleted=True)
    return HttpResponseRedirect("/tasks")

def complete_task_view(request, index):
    Task.objects.filter(id=index).update(completed=True)
    return HttpResponseRedirect("/tasks")

def completed_tasks(request):
    completed_list= Task.objects.filter(deleted=False).filter(completed=True)
    return render(request, "completed.html", {"completed":completed_list})

def all_tasks_view(request):
    tasks_list= Task.objects.filter(deleted=False).filter(completed=False)
    completed_list= Task.objects.filter(deleted=False).filter(completed=True)
    return render(request, "all.html", {"tasks":tasks_list, "completed":completed_list})
