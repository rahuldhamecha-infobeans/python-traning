from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage


# Create your views here.

def index(request):
    webpages = AccessRecord.objects.order_by('date')
    my_dict = {'name': 'Hello, I\'m Rahul Dhamecha','webpages':webpages}
    return render(request,'first_app/index.html',my_dict)

def first_app(request):
    return HttpResponse('Test File')

def test_route(request):
    return HttpResponse('Test Route File')

def help(request):
    my_content = {'page_name' : 'Help Page','page_content' : 'This is the Help Page.'}
    return render(request,'first_app/help.html',my_content)