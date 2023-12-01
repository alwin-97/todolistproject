from django.shortcuts import render, redirect

from .models import ToDoList

# Create your views here.
def index(request):
    if request.POST:
        new_task = request.POST['task'].strip()
        new_desc = request.POST['description']
        todolist = ToDoList(task_title=new_task,task_description=new_desc)
        todolist.save()
        return redirect('index')

    todolist = ToDoList.objects.all()
    return render(request,
                  'todolist/index.html',
                  context={'tasks': todolist})
