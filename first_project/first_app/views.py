from django.http import HttpResponse
from django.shortcuts import render
from first_app.models import *

# Create your views here.
# def index(request):
#     return HttpResponse("<h1>Hello Murali!!!</h1>")

def index(request):
    index_dict = {'insert_me': 'Welcome Murali!!!'}
    return render(request, 'first_app/index.html', context=index_dict)

def profile(request):
    profile_dict = {}
    return render(request, 'first_app/profile.html', context=profile_dict)

def pageslist(request):
    Webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': Webpage_list}
    return render(request, 'first_app/page.html', context=date_dict)