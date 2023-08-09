from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hof(request):
    return render(request, 'index.html')


    