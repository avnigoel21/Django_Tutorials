from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Student(models.Model):
    # id = models.AutoField()
    name  = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField( null = True , blank=True)

class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name

# CRUD - CREATE , READ , UPDATE, DELETE


# signals :  pre_save , post_save , pre_delete , post_delete

# cars.com/get_speed/?car_name = Nexon
# {
#     car_speed : 120
# }

# @receiver(post_save , Sender = Car)
# def call_car_api(sender , instance , **kwargs):
#     print("Request finished!")
