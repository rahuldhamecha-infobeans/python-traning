from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage
from . import forms
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    webpages = AccessRecord.objects.order_by('date')
    my_dict = {'name': 'Hello, I\'m Rahul Dhamecha','webpages':webpages}
    return render(request,'first_app/index.html',my_dict)

@login_required
def first_app(request):
    return HttpResponse('Test File')

@login_required
def test_route(request):
    return HttpResponse('Test Route File')

def help(request):
    my_content = {'page_name' : 'Help Page','page_content' : 'This is the Help Page.'}
    return render(request,'first_app/help.html',my_content)

@login_required
def form_view(request):
    form = forms.MyForm()

    if request.method == "POST":
        form = forms.MyForm(request.POST)

        if form.is_valid():
            print('Validate Successfully!')
            print("Name : {}".format(form.cleaned_data['name']))
            print("Email : {}".format(form.cleaned_data['email']))
            print("Text : {}".format(form.cleaned_data['text']))

    return render(request,'first_app/forms.html',{'form':form})