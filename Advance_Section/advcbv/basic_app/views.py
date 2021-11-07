from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return render(request, 'basic_app/homepage.html')

# class CBView(View):
#     def get(self, request):
#         return HttpResponse("From Class based views!!!")

class IndexView(TemplateView):
    template_name = "basic_app/homepage.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['injectme'] = 'Murali'
        return context