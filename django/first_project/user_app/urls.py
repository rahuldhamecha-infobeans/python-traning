from django.urls import path, re_path
from user_app import views

app_name = "users"

urlpatterns = [
    re_path(r'^$',views.index,name='user_index'),
    path('forms/',views.register,name='user_registration')
]