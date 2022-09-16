from django.db import models
#Напишите тип данных каждого из перечисленных типов моделей django.
# models.BooleanField() булеан
# models.DateTimeField() строка
# models.FloatField() число
# models.CharField() строка
# models.EmailField() строка
# models.TextField() строка

class ToMeet(models.Model):
    persone = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    date_of_meeting = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True) # чтобы не всегда заполнять 
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
