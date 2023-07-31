from django.urls import path, re_path
from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    path("register/",views.register,name='register'),
    path("login/",views.user_login,name='login'),
    path("logout/",views.user_logout,name='logout'),
    path("special/",views.special,name='special'),
]