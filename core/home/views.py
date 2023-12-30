from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("<h1>Hey I am Django server</h1>")
    peoples=[
        {"name":"Sunil K","age":14},
        {"name":"Abhjit","age":30},
        {"name":"Jyoti","age":32}
    ]

    vegetables=["pumpkin","tomato"]
    return render(request,"index.html",context={'peoples':peoples,'page':'Home'})

def about(request):
    context={'page':'About'}
    return render(request,"about.html",context)

def contact(request):
    context={'page':'Contact'}
    return render(request,"contact.html")

def success_page(request):
    return HttpResponse("<h1> Hi, this is success page</h1>")