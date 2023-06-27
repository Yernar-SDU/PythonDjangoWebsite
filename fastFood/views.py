from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from fastFood.forms import RegisterForm, LoginForm
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
            form.save()
            return redirect('/')
        else:
            form = RegisterForm(request.POST)
    else:
        form = RegisterForm()

    return render(request, 'register.html', context={'form': form})


def login_view(request):
    form = LoginForm()
    error = False
    if request.method == 'POST': # Button login
        error = False
        print('post method')
        form = LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            print('form valid')

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)

            user = authenticate(username=username, password=password)
            if user is not None: #user exist, succesfull
                print('user exist, login')
                login(request, user)
                return redirect('/')
            else: # user doesn't exist
                print('user don\'t exits')
                error = True
                messages.error(request, "The username doesn\'t exists")
                form = LoginForm(request.POST)

        else:
            print('form is invalid')
            error = True
            messages.error(request, "Invalid form")
    return render(request, 'login.html', context={'form': form, 'error': error})
