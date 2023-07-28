from django.shortcuts import render
from user_app.models import User
# Create your views here.

def index(request):
    users = User.objects.order_by('first_name')
    user_content = {'users' : users}
    return render(request,'user_app/index.html',user_content)