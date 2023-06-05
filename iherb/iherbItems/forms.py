from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Item


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ItemDetailsChangeForm(forms.ModelForm):
    """A published book."""
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    factory = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control'}))
    weight = forms.IntegerField(help_text='The weight of the item', widget=forms.TextInput(attrs={'class': 'form-control'}))
    codeNumber = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    upcNumber = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(help_text='The count inside one package', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=100000, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=False)

    class Meta:
        model = Item
        fields = ['title', 'factory', ]

class ItemCreateForm(forms.ModelForm):
    """A published book."""
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    factory = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control'}))
    expiration_date = forms.DateTimeField(
        label='Enter Date and Time',
        input_formats=['%Y-%m-%d'],
        widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD'})
    )
    available_date = forms.DateTimeField(
        label='Enter Date and Time',
        input_formats=['%Y-%m-%d'],
        widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD'})
    )
    weight = forms.IntegerField(help_text='The weight of the item', widget=forms.TextInput(attrs={'class': 'form-control'}))
    codeNumber = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    upcNumber = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    size = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=100000, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=False)

    class Meta:
        model = Item
        fields = ['title', 'factory', ]
