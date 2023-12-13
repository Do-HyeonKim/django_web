from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def hello_word(request) : 
    # return HttpResponse('hello world')
    return render(request,'base.html') #template name