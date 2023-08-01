from django.urls import path, re_path
from advanced_app import views

app_name = "advanced"

urlpatterns = [
    re_path(r'^$',views.IndexView.as_view(),name='index'),
    path('schools/',views.SchoolListView.as_view(),name='school'),
    path('students/',views.StudentListView.as_view(),name='student'),
    re_path(r"^schools/(?P<pk>\d+)/$", views.SchoolDetailView.as_view(),name='school_detail'),
    re_path(r"^student/(?P<pk>\d+)/$", views.StudentDetailView.as_view(),name='student_detail'),
    path('schools/create',views.SchoolCreateView.as_view(),name='create_school'),
    re_path(r"^schools/update/(?P<pk>\d+)/$", views.SchoolUpdateView.as_view(),name='school_update'),
    re_path(r"^schools/delete/(?P<pk>\d+)/$", views.SchoolDeleteView.as_view(),name='school_delete'),
    path('student/create',views.StudentCreateView.as_view(),name='create_student'),
    re_path(r"^student/update/(?P<pk>\d+)/$", views.StudentUpdateView.as_view(),name='student_update'),
    re_path(r"^student/delete/(?P<pk>\d+)/$", views.StudentDeleteView.as_view(),name='student_delete'),
]