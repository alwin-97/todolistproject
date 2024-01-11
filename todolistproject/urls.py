"""
URL configuration for todolistproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from todolist.views import index, deleteTask, editTask
from authsystem.views import login_page, admin_dashbord

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', index, name='index'),
    # path('edit/<str:id>',editTask,name='edit-task'),
    # path('delete/<str:id>',deleteTask,name='delete-task'),

    path('',login_page,name='login'),
    path('admin-dashborad',admin_dashbord,name='admin-dashboard'),
]
