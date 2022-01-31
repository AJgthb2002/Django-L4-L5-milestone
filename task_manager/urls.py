from operator import index
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

tasks_list=[]
completed_list=[]

def tasks_view(request):
    return render(request, "tasks.html", {"tasks":tasks_list})

def add_task_view(request):
    task_value= request.GET.get("task")
    tasks_list.append(task_value)
    return HttpResponseRedirect("/tasks")

def delete_task_view(request, index):
    tasks_list.pop(index-1)
    return HttpResponseRedirect("/tasks")

def complete_task_view(request, index):
    completed_list.append(tasks_list[index-1])
    tasks_list.pop(index-1)
    print(completed_list)
    return HttpResponseRedirect("/tasks")

def completed_tasks(request):
    return render(request, "completed.html", {"completed":completed_list})

def all_tasks_view(request):
    return render(request, "all.html", {"tasks":tasks_list, "completed":completed_list})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', tasks_view),
    path('addtask/', add_task_view),
    path('delete_task/<int:index>/', delete_task_view),
    path('complete_task/<int:index>/', complete_task_view),
    path('completed_tasks/', completed_tasks),
    path('all_tasks/', all_tasks_view)
]

