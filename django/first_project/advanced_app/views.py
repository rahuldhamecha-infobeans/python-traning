from django.shortcuts import render
from django.views.generic import View,TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'advanced_app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Advanced Page'
        return context
