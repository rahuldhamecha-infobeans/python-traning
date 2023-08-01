from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models
# Create your views here.
class IndexView(TemplateView):
    template_name = 'advanced_app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Advanced Page'
        return context

class SchoolListView(ListView):
    template_name = 'advanced_app/school_list.html'
    # by default school_list variable return in ListView (MODELNAME_list)
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'advanced_app/details.html'
