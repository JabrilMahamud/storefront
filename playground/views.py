from django.shortcuts import render
from django.http import HttpResponse
from .s3dictionary import dictionaryCreator

# Create your views here.
#this is the request handler
#turns requests into responses

def  say_hello(request):
    return render(request, 'hello.html',{'name':'Jabril'})

def s3RequestHandler(request):
       return render(request,'jsonDisplay.html',dictionaryCreator())
    