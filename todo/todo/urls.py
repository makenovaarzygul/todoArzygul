"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from main.views import homepage, test, check,add_todo
from homework.views import homework,newf,meeting,add_tomeet
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path('test/',test,name="test"),
    path('homework/',homework,name="homework"),
    path('newf/',newf,name="newf"),
    path('check/',check),
    path('meeting/',meeting,name="meeting"),
    path('add-todo/',add_todo,name="add-todo"),
    path('add-tomeet/',add_tomeet,name="add-tomeet")
]  +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) \
   +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
