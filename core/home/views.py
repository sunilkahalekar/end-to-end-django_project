from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("<h1>Hey I am Django server</h1>")
    return render(request,"index.html")

def success_page(request):
    return HttpResponse("<h1> Hi, this is success page</h1>")