from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homework(request):
    return render(request,"homework.html")
   
def newf(request):
    return HttpResponse("Добро пожаловать в приложение ToDo - Admin")