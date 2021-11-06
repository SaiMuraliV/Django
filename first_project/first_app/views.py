from django.http import HttpResponse
from django.shortcuts import render
from first_app.models import *
from first_app.forms import UserForm

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


def formpage(request):
    form =  UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            # data accessing 
            print("Validation success!!")
            print("name : "+ form.cleaned_data['name'])
            print("email : "+ form.cleaned_data['email'])
            print("text : "+ form.cleaned_data['text'])
    return render(request, 'first_app/forms_page.html',{'form': form})