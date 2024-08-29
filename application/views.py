from django.shortcuts import render, get_object_or_404, redirect
from .models import *



def home(request):
    return render(request, "main.html")

def contact(request):
    return render(request,"contact.html")