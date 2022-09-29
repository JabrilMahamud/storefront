from distutils.log import error
from json import loads
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .s3dictionary import tableDict
from flask import jsonify
from json2html import *
# Create your views here.
#this is the request handler
#turns requests into responses


####actual views part of the file
def  say_hello(request):
    return render(request, 'hello.html',{'name':'Jabril'})

def s3RequestHandler(request):
    return render(request,'jsonDisplay.html',tableDict)
def s3responseHandler(response):
    return render(response,)