from django.urls import path, re_path
from advanced_app import views

app_name = "advanced"

urlpatterns = [
    re_path(r'^$',views.IndexView.as_view(),name='index'),
    path('schools/',views.SchoolListView.as_view(),name='school'),
    path('students/',views.SchoolListView.as_view(),name='student'),
    re_path(r"^schools/(?P<pk>\w+)/$", views.SchoolDetailView.as_view(),name='school_detail'),
]