from django.shortcuts import render , redirect
from .models import *

from django.http import HttpResponse

# Create your views here.


def receipes(request):
    if request.method == "POST":

        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_image = receipe_image,
            receipe_description = receipe_description,
            receipe_name = receipe_name
        )

        return redirect('/receipes/')
    
    queryset = Receipe.objects.all()
    context = {'receipes' : queryset}

    return render(request , "receipes.html" , context)


def delete_receipes(request, id):
   queryset = Receipe.objects.get(id = id)
   queryset.delete()
   return redirect('/receipes/')