from django.shortcuts import render

from fastFood.forms import RegisterForm
from fastFood.models import Food


# Create your views here.
def home_page(request):
    foods = Food.objects.all()
    return render(request, 'index.html', context={'foods': foods})


def food_details(request, food_id):
    food = Food.objects.get(id=food_id)
    return render(request, 'food_details.html', context={'food': food})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            1.save the user
            2. redirect for login page
        else:
            form = RegisterForm(request.POST)
    else:
        form = RegisterForm()

    return render(request, 'register.html', context={'form': form})
