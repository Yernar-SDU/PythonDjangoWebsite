import json

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, ItemDetailsChangeForm, ItemCreateForm, ItemSearchForm
from .models import Item, ItemEncoder
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core import serializers

from .utils import FixedSizeStack, RECENT_VIEWED_ITEMS_QUEUE, DjangoModelEncoder, default_items


def user_is_admin(user):
    return user.is_superuser

@login_required(login_url="/login")
def home_page(request):

    items = Item.objects.all()
    return render(request, 'ogani-master/index.html', context={'items': items})

@user_passes_test(user_is_admin, login_url='/login')
@staff_member_required
def admin_view(request):
    items = Item.objects.all()
    print(items)
    return render(request, 'ogani-master/admin.html', context={'items': items})


def item_details(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.user.is_authenticated:
        queue = request.session.get(RECENT_VIEWED_ITEMS_QUEUE, [])
        if len(queue) == 3:
            queue.pop(0)
            queue.append(item.pk)
        else:
            queue.append(item.pk)
        request.session[RECENT_VIEWED_ITEMS_QUEUE] = queue
        request.session.save()

    return render(request, 'ogani-master/item-details.html', context={"item": item})


def item_details_admin(request, item_id):
    form = ItemDetailsChangeForm()
    if request.method == 'POST':
        form = ItemDetailsChangeForm(request.POST, request.FILES)
        print("item_details_admin_post_method")
        if form.is_valid():
            print("item_details_admin_form_isvalid")
            item = Item.objects.get(id=item_id)
            item.title = form.cleaned_data['title']
            item.factory = form.cleaned_data['factory']
            item.weight = form.cleaned_data['weight']
            item.codeNumber = form.cleaned_data['codeNumber']
            item.upcNumber = form.cleaned_data['upcNumber']
            item.quantity = form.cleaned_data['quantity']
            item.category = form.cleaned_data['category']
            item.description = form.cleaned_data['description']
            item.price = form.cleaned_data['price']
            if 'image' in form.changed_data:
                item.image = form.cleaned_data['image']
            item.save()
            items = Item.objects.all()
            return render(request, 'ogani-master/admin.html', context={'items': items})
        else:
            print("YernarERRORS: ", str(form.errors))
            print(form.non_field_errors())
            messages.error(request, "Invalid username or password.")

    item = get_object_or_404(Item, id=item_id)
    form.initial['title'] = item.title
    form.initial['factory'] = item.factory
    form.initial['weight'] = item.weight
    form.initial['codeNumber'] = item.codeNumber
    form.initial['upcNumber'] = item.upcNumber
    form.initial['quantity'] = item.quantity
    form.initial['category'] = item.category
    form.initial['description'] = item.description
    form.initial['price'] = item.price
    form.initial['image'] = item.image

    # form.factory = "asdf"
    return render(request, 'ogani-master/admin-details.html', {'item': item, 'form': form})


def new_item_admin(request):
    form = ItemCreateForm()
    if request.method == 'POST':
        form = ItemCreateForm(request.POST, request.FILES)
        if form.is_valid():
            item = Item()
            item.title = form.cleaned_data['title']
            item.factory = form.cleaned_data['factory']
            item.weight = form.cleaned_data['weight']
            item.codeNumber = form.cleaned_data['codeNumber']
            item.upcNumber = form.cleaned_data['upcNumber']
            item.quantity = form.cleaned_data['quantity']
            item.category = form.cleaned_data['category']
            item.description = form.cleaned_data['description']
            item.price = form.cleaned_data['price']
            item.available_date = form.cleaned_data['available_date']
            item.expiration_date = form.cleaned_data['expiration_date']
            item.size = form.cleaned_data['size']
            if 'image' in form.changed_data:
                item.image = form.cleaned_data['image']
            item.save()
            items = Item.objects.all()
            return render(request, 'ogani-master/admin.html', context={'items': items})
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'ogani-master/admin-details.html', context={'form': form})


def remove_item_admin(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        item.delete()
        return redirect('myadmin_page')
    except Item.DoesNotExist:
        return redirect('myadmin_page')


def login_page(request):
    return render(request, 'ogani-master/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        print('Home page')
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'ogani-master/register.html', context)


def login_view(request):
    form = AuthenticationForm()
    error = False
    if request.method == "POST":
        print("post")
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("valid form")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                error = True
                messages.error(request, "Invalid username or password.")
        else:
            error = True
            messages.error(request, "Invalid username or password.")
    return render(request=request, template_name='ogani-master/login.html', context={"form": form, "error": error})


def logout_view(request):
    logout(request)
    return redirect("/")


def shop(request):
    items = Item.objects.all()
    searchForm = ItemSearchForm(request.GET)
    searchQuery = searchForm['search_query'].value()
    recentItems = []
    if request.user.is_authenticated:
        queue = request.session.get(RECENT_VIEWED_ITEMS_QUEUE, [])
        for pk in queue:
            item = Item.objects.get(id=pk)
            recentItems.append(item)


    if searchQuery:
        items = Item.objects.filter(title__icontains=searchQuery)


    category = request.GET.get('category')
    return render(request, 'ogani-master/shop.html',
                  context={'items': items, 'category': category, 'searchForm': searchForm, 'recentItems': recentItems[::-1]})

