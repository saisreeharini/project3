from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def string_Response(request):
    return HttpResponse('this is my first string')
    

