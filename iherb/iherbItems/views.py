from django.shortcuts import render
from .models import Item


# Create your views here.
def home_page(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'ogani-master/index.html', context)
