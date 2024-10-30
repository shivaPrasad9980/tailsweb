from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.logIn,name="index"),
    path('home/',views.home,name="home"),
    path('logout/',views.logOut,name='logout'),
    path('add_student',views.add_student,name="add_student"),
    path('delete/<int:id>/',views.deleteStudent,name='delete'),
    path('update/<int:id>/',views.updateStudent,name='update')
    ]