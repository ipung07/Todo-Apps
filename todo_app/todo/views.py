from django.shortcuts import render, redirect
from . models import Todo
from . forms import TodoForm
# Create your views here.


def index(request):
    todo = Todo.objects.all()
    context = {
        'todos': todo,
    }
    return render(request, 'todo/index.html', context=context)


def detail(request, id):
    todo = Todo.objects.get(pk=id)
    context = {
        'todo': todo,
    }
    return render(request, 'todo/detail.html', context=context)


def insert(request):
    form = TodoForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/todo/")
        else:
            form = TodoForm()
    else:
        context = {
            'form': form,
        }
        return render(request, 'todo/insert.html', context=context)


def edit(request, id):
    instance = Todo.objects.get(pk=id)
    form = TodoForm(request.POST or None,
                    request.FILES or None, instance=instance)
    if request.method == 'POST':
        if request.FILES.get('todo_image') != None:
            instance.todo_image.delete(save=True)
        if form.is_valid():
            form.save()
            return redirect('/todo/')
    else:
        context = {
            'form': form,
            'todo': instance,
        }
        return render(request, 'todo/edit.html', context=context)


def delete(request, id):
    if request.method == 'POST':
        id = request.POST['id_todo']
        todo = Todo.objects.get(pk=id)
        image = todo.todo_image
        if image is not "default.jpg":
            image.delete(save=True)
        todo.delete()
        return redirect("/todo")
