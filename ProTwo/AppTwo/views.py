from django.shortcuts import render
from django.http import HttpResponse

from AppTwo.models import UserInfo
from AppTwo.forms import NewUserForm

# Create your views here.
# def index(request):
#     return HttpResponse("<h1><em>My Second App</em></h1>")


def homepage(request):
    homepage_dict = {"insert_name": "Hai Murali"}
    return render(request, "homepage.html", context=homepage_dict)


def help(request):
    help_dict = {"insert_name": "Hai Murali"}
    return render(request, "AppTwo/help.html", context=help_dict)


def user(request):
    user = UserInfo.objects.order_by("fname")
    user_dict = {"user_data": user}
    return render(request, "AppTwo/user.html", context=user_dict)

def signup(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            
            return homepage(request)
        
        else:
            print("Error form invalid")
    return render(request, "AppTwo/signup.html", {'form': form})
            