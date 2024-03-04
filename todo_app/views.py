from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    # print(request.POST['task'])
    task = request.POST['task']
    Task.objects.create(task=task)
    # return HttpResponse('form submitted')
    return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Task,pk=pk)
    # print(task)
    # return HttpResponse(task)
    task.is_completed = True
    task.save()
    return redirect('home')
    