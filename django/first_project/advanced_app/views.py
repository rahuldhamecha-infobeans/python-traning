from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from . import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'School List'
        return context
class StudentListView(ListView):
    template_name = 'advanced_app/student_list.html'
    # by default school_list variable return in ListView (MODELNAME_list)
    context_object_name = 'students'
    model = models.Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Student List'
        return context

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'advanced_app/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'School Detail'
        return context

@method_decorator(login_required,name='dispatch')
class SchoolCreateView(CreateView):
    model = models.School
    fields = ("name","principal","location")
    template_name = 'advanced_app/school_add_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Create School'
        return context

@method_decorator(login_required,name='dispatch')
class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    model = models.School
    template_name = 'advanced_app/school_add_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Update School'
        return context

@method_decorator(login_required,name='dispatch')
class SchoolDeleteView(DeleteView):
    context_object_name = 'school'
    model = models.School
    success_url = reverse_lazy('advanced:school')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Delete School'
        return context

# Student Details View
class StudentDetailView(DetailView):
    context_object_name = 'student_detail'
    model = models.Student
    template_name = 'advanced_app/student_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Student Detail'
        return context

@method_decorator(login_required,name='dispatch')
class StudentCreateView(CreateView):
    model = models.Student
    fields = ("name","age","school")
    template_name = 'advanced_app/student_add_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Create Student'
        return context

@method_decorator(login_required,name='dispatch')
class StudentUpdateView(UpdateView):
    fields = ("name", "age", "school")
    model = models.Student
    template_name = 'advanced_app/student_add_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Update Student'
        return context

@method_decorator(login_required,name='dispatch')
class StudentDeleteView(DeleteView):
    context_object_name = 'student'
    model = models.Student
    # success_url = reverse_lazy("advanced:school")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Delete Student'
        return context

    def get_success_url(self):
        return reverse_lazy('advanced:school_detail', kwargs={'pk': self.object.school.pk})