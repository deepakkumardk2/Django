from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    date = datetime.datetime.now()
    print("test function is called from view")
    #return HttpResponse("<h1>Hello, I have started Django Python framework</h1>" + str(date))
    return render(request,"home.html",{})
def about(request):
    #return HttpResponse("<h1>This is my learning journey of Django framework</h1>")
    return render(request,"about.html",{})
def services(request):
    #return HttpResponse("<h1>This is my learning journey of Django framework ,This page belong services page </h1>")
    return render(request,"services.html",{})