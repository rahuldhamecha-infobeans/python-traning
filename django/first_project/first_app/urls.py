from django.urls import path, re_path
from first_app import views

urlpatterns = [
    re_path(r'^$',views.first_app,name='first_app'),
    path('test/',views.test_route,name='test_route')
]