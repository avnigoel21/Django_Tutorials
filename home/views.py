import random
from django.shortcuts import render , redirect

from django.http import HttpResponse

from .utils import *
from django.conf import settings
from home.models import Car

# Create your views here.


def send_email(request):
    subject = "This email is from Django server with Attachment"
    message = "This is a test message from django with attach file"
    recipient_list = ["avnigoel.volunteer@gmail.com"]
    file_path = f'{settings.BASE_DIR}/main.xlsx'
    send_email_with_attachment(subject , message , recipient_list , file_path)
    return redirect("/")

def home(request):
    # return HttpResponse("hey, i am django server")

    Car.objects.create(car_name = f'Nexon-{random.randint(0 , 50)}')

    peoples = [
        {'name' : 'Avni' , 'age' : 26},
        {'name' : 'Aditi' , 'age' : 18},
        {'name' : 'Avantika' , 'age' : 6},
        {'name' : 'deepanshu' , 'age' : 36},
        {'name' : 'sandeep' , 'age' : 26}
    ]

    vegetables = ['pumpkin' , 'tomato' , 'potato']

    text = """
    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam impedit illo necessitatibus esse iste natus, vitae quasi asperiores molestiae. Unde voluptate, minus impedit sint velit vel mollitia architecto veniam. Consequatur, aliquam, quos maiores quisquam facilis earum explicabo animi vel maxime inventore incidunt fugiat dolorem cupiditate placeat voluptates et aspernatur tempore alias eveniet? Sequi odio ea incidunt et nemo eaque sunt placeat alias est, similique quisquam asperiores corrupti cumque debitis dolores ullam esse quam quia, odit sit adipisci? 
    """

    return render(request, "home/index.html" , context = {'page' : 'Django Website' , 'peoples' : peoples,  'text' : text , 'vegetables' : vegetables})


def contact(request):
    context = {'page'  : 'Contact'}
    return render (request , "home/contact.html" , context)
