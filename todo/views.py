# from django.shortcuts import render, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
# from todo.models import Task
# from users.models import NewUser
# from users.views import *
# from todo.forms import *
# from django.db import transaction
# from django.urls import reverse_lazy    


# # CRUD
# # C => CREATE
# # R => READ / RETRIEVE
# # u => UPDATE
# # D => DELETE

# # Create your views here.
# @login_required
# def todo_list(request):
#     todos = Task.objects.filter(user=request.user)
#     return render(
#         request = request,
#         template_name = "todo_list.html",
#         context = {"todos": todos},
#     )

# # To make the button work
# @login_required
# def todo_create(request):
#     if request.method == "POST":
#         title = request.POST.get('title', '')
#         if title:
#             # ORM => Object Relational Mapping
#             Task.objects.create(title=title, user=request.user)
#             return HttpResponseRedirect("todo_list.html")
#     return render(request, "todo_create.html")

# @login_required
# def todo_delete(request, pk):
#     todo = Task.objects.get(id=pk, user=request.user) # pk is primary key (id)
#     todo.delete()
#     return HttpResponseRedirect("todo_list.html")

# @login_required
# def todo_update(request, pk):
#     todo = Task.objects.get(id = pk, user=request.user)
#     if request.method == "POST":
#         title = request.POST["title"]
#         todo = Task.objects.get(id = pk, user=request.user)
#         todo.title = title
#         todo.save()
#         return HttpResponseRedirect("todo_list.html")
    
#     return render(
#                     request, 
#                     "todo_update.html",
#                     {"todo": todo},
#                 )

# def task_reorder(request):
#     form = PositionForm(request.POST)
#     if form.is_valid():
#         positionList = form.cleaned_data["position"].split(',')

#         with transaction.atomic():
#             request.user.set_task_order(positionList)

#     return redirect(reverse_lazy('tasks'))

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import transaction

from .forms import *
from .models import Task

def todo_list(request):
    tasks = Task.objects.filter(user=request.user.id)
    count = tasks.filter(complete=False).count()

    search_input = request.GET.get('search-area') or ''
    if search_input:
        tasks = tasks.filter(title__contains=search_input)

    context = {
        'tasks': tasks,
        'count': count,
        'search_input': search_input,
    }
    return render(request, 'todo_list.html', context)

def todo_detail(request, pk):
    task = Task.objects.get(pk=pk)
    context = {
        'task': task
    }
    return render(request, 'todo.html', context)

def todo_create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            task = form.save(commit=True)
            task.user = request.user
            task.save()
            return redirect('todos')
    else:
        form = CreateForm()
    return render(request, 'todo_create.html', {'form': form})

def todo_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('todo-list')
    else:
        form = UpdateForm(instance=task)
    return render(request, 'todo_update.html', {'form': form})

def todo_delete(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteForm(request.POST, instance=task)
        if form.is_valid():
            task.delete()
            return redirect('todos')
    else:
        form = DeleteForm(instance=task)
    return render(request, 'todo_delete.html', {'form': form})

 

# def todo_reorder(request):
#     if request.method == 'POST':
#         form = PositionForm(request.POST)
#         if form.is_valid():
#             position_list = form.cleaned_data["position"].split(',')

#             with transaction.atomic():
#                 request.user.set_task_order(position_list)

#     return redirect('todos')
