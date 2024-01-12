from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from authsystem.models import userdetails


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
            return redirect('login')
    return render(request,'authpages/login.html')

def admin_dashbord(request):
    return render(request,'todolist/dashboard.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        role = request.POST['role']
        user = User(first_name=name, username=email, email=email, password=make_password(password))
        user.save()
        user_details = userdetails(user_id=user.id,user_phone=phone,user_type=role)
        user_details.save()
        return redirect('login')
    return render(request,'authpages/register.html')