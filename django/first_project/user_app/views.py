from django.shortcuts import render
from user_app.models import User
from user_app.forms import UserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    page_name = 'Users'
    users = User.objects.order_by('id')
    user_content = {'users' : users,'page_title' : page_name}
    return render(request,'user_app/index.html',user_content)

@login_required
def register(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")

    return render(request,'user_app/forms.html',{'form':form})