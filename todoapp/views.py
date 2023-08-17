from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task
from django.http import JsonResponse
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    pendingTasks = Task.objects.filter(completed=False)
    completedTasks = Task.objects.filter(completed=True)
    context = {'tasks': tasks, 'pendingTasks': pendingTasks, 'completedTasks': completedTasks}
    return render(request, 'home.html', context)

def addTask(request):
    task = request.POST['task']
    newTask = Task(title=task)
    newTask.save()
    return redirect(reverse('index'))

def completeTask(request, id):
    completedTask = Task.objects.get(id=id)
    completedTask.completed = True
    completedTask.save()
    return redirect(reverse('index'))

def deleteTask(request, id):
    deletedTask = Task.objects.get(id=id)
    deletedTask.delete()
    return redirect(reverse('index'))