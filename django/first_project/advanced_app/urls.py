from django.urls import path, re_path
from advanced_app import views

app_name = "advanced"

urlpatterns = [
    re_path(r'^$',views.IndexView.as_view(),name='index'),
]