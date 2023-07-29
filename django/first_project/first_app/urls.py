from django.urls import path, re_path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    re_path(r'^$',views.index,name='first_app'),
    path("test/",views.test_route,name='test_route'),
    path("forms/",views.form_view,name='form_view')
]