from django.http import HttpResponse
from django.shortcuts import render
from .models import ToMeet


def homework(request):
    return render(request,"homework.html")
   
def newf(request):
    return HttpResponse("Добро пожаловать в приложение ToDo - Admin")

def meeting(request):
    tomeet_list = ToMeet.objects.all()
    return render(request,"meeting.html",{"tomeet_list": tomeet_list})
