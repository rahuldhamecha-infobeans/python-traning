from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'name': 'Hello, I\'m Rahul Dhamecha'}
    return render(request,'first_app/index.html',my_dict)

def first_app(request):
    return HttpResponse('Test File')

def test_route(request):
    return HttpResponse('Test Route File')

def help(request):
    my_content = {'page_name' : 'Help Page','page_content' : 'This is the Help Page.'}
    return render(request,'first_app/help.html',my_content)