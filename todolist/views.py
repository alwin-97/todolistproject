from django.shortcuts import render, redirect

# will store the tasks that are added
todolist = []


# Create your views here.
def index(request):
    if request.POST:
        new_task = request.POST['task']
        todolist.append(new_task.strip())
        return redirect('index')

    return render(request,
                  'todolist/index.html',
                  context={'tasks': todolist})
