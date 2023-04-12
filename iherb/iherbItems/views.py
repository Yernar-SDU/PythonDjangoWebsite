from django.shortcuts import render
from .models import Item


# Create your views here.
def home_page(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'ogani-master/index.html', context)


def login_page(request):
    return render(request, 'ogani-master/login.html')
