from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm, UpdateTaskForm

# Create your views here.
def index(request):
    todos = Task.objects.all()
    count_todos = todos.count()

    completed_todo = Task.objects.filter(complete=True)
    count_completed_todo = completed_todo.count()

    count_uncompleted_todo = count_todos - count_completed_todo

    percentageoftaskscompleted = int((count_completed_todo/count_todos) * 100)

    if request.method=='POST':
       form = TaskForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/')
    else:
        form = TaskForm() 
    context = {
        'todos': todos,
        'form' : form,
        'count_todos': count_todos,
        'count_completed_todo': count_completed_todo,
        'count_uncompleted_todo': count_uncompleted_todo,
        'percentageoftaskscompleted': percentageoftaskscompleted
    }
    return render(request, 'todoapp/todo/index.html', context)

def update(request, pk):
    todo = Task.objects.get(id=pk)
    if request.method=="POST":
        form = UpdateTaskForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo-index')
    else:
        form = UpdateTaskForm(instance=todo)
    context = {
        'form':form
    }
    return render(request, 'todoapp/todo/update.html', context)

def delete(request, pk):
    todo = Task.objects.get(id=pk)
    if request.method=='POST':
        todo.delete()
        return redirect('todo-index')
    return render(request, 'todoapp/todo/delete.html')