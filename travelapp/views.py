from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from django.db.models import Q
from account .models import *
# Create your views here.
def fun(request):
    obj=place.objects.all()

    return render(request,"index.html",{'results':obj})
def about(request):
    return render(request,"about.html")
