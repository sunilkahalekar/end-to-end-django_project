from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def receipes(request):
    if request.method=="POST":
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
        # to get data and save
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
        )
        return redirect('/receipes/')
        print(receipe_name)
        print(receipe_description)
        print(receipe_image)
    return render(request,'receips.html')