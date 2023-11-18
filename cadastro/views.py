from django.shortcuts import render
from setup import urls

def base(request):
    return render(request, 'base.html')

def base2(request):
    return render(request, 'base2.html')