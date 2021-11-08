from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from basic_app import models

# Create your views here.
# def index(request):
#     return render(request, 'basic_app/homepage.html')

# class CBView(View):
#     def get(self, request):
#         return HttpResponse("From Class based views!!!")

class IndexView(TemplateView):
    template_name = "homepage.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['injectme'] = 'Murali'
        return context
    
# ListView will use the "<model name in lowercase>_list" and 
class SchoolListView(ListView):
    # ListView will return "school_list" for model
    # or 
    # we can is context_object_name
    context_object_name = 'schools'
    model = models.School
    
    # template_name = 'basic_app/school_list.html'
    
class SchoolDetailView(DetailView):
    # Detailview will return "school" for model
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
    