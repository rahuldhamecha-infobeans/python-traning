from django.shortcuts import render
from auth_app.forms import UserProfileInfoForm, UserForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse,resolve
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    page_name = 'Auth App'
    return render(request, 'auth_app/index.html', {'page_name': page_name})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("Your Are Logged in, Nice")

def register(request):
    user_form = UserForm()
    user_profile_form = UserProfileInfoForm()
    page_name = 'Register'
    is_registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = user_profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            is_registered = True
        else:
            print(user_form.errors, user_profile_form.errors)

    template_data = {
        'registered': is_registered,
        'page_name': page_name,
        'user_form': user_form,
        'user_profile_form': user_profile_form
    }

    return render(request, 'auth_app/register.html', template_data)


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                next_url = request.GET
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE!')
        else:
            print('Someone tried to login and failed.')
            print("Username : {} and Password : {}".format(username,password))
            return HttpResponse("Invalid Login!")

    template_data = {
        'page_name': 'Login',
    }
    return render(request, 'auth_app/login.html', template_data)
