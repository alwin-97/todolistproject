from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin-dashboard')
        else:
            pass
    return render(request,'authpages/login.html')

def admin_dashbord(request):
    return render(request,'todolist/dashboard.html')