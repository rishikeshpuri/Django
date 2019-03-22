from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def namestay_homePage(request):
    return HttpResponse('namestay means HELLO in Hindi!')
