from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .forms import TaskForm

def show_tasks(request):
    tasks = models.TaskModel.objects.filter(is_completed=False)
    return render(request, "./index.html", {'tasks_list': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
        
        return redirect("show_tasks") 
    
    else:
        form = TaskForm()
        return render(request, './add.html', {'form':form})


def delete_task(request, task_id):
    task = models.TaskModel.objects.get(pk = task_id).delete()
    return redirect("show_tasks") 


def edit_task(request, task_id):
    task = models.TaskModel.objects.get(pk = task_id)
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form_edited = TaskForm(request.POST, instance=task)
        if form_edited.is_valid():
            form_edited.save()
            print(form_edited.cleaned_data)

        return redirect("show_tasks") 
    
    return render(request, './edit.html', {'form':form})

def make_complete_task(request, task_id):
    task = models.TaskModel.objects.get(pk = task_id)
    task.is_completed = True
    task.save()

    return redirect("complete_tasks") 


def complete_tasks(request):
    tasks = models.TaskModel.objects.filter(is_completed=True)
    return render(request, "./complete.html", {'tasks_list': tasks})