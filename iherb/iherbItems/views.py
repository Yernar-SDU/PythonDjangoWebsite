from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Item
from django.contrib.auth import authenticate, login


# Create your views here.
def home_page(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'ogani-master/index.html', context)


def login_page(request):
    return render(request, 'ogani-master/login.html')

@login_required(login_url="")
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # A backend authenticated the credentials
        ...
    else:
        # No backend authenticated the credentials
        ...