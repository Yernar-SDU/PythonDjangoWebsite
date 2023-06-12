import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models


# Create your models here.
class Item(models.Model):
    """A published book."""
    title = models.CharField(
        max_length=200,
        help_text="The title of the book.")
    factory = models.CharField(
        max_length=70, help_text='Builed factory name',
        default='ChildLife'
    )
    expiration_date = models.DateField(
        verbose_name="Date the item will expire.")
    available_date = models.DateField(
        verbose_name="Date the item will be available.")
    weight = models.IntegerField(help_text='The weight of the item')
    codeNumber = models.CharField(
        max_length=100,
        help_text='The code of the product',
        default=3245425324
    )
    upcNumber = models.CharField(
        max_length=100,
        help_text='The UPC number of the product',
        default='32454654234'
    )
    quantity = models.IntegerField(
        help_text='The count inside one package',
        default=20
    )

    size = models.CharField(max_length=200, help_text='The size of item in inches', default=12)

    category = models.CharField(max_length=200, help_text='Trend, Bestseller or something', default='Bestseller')

    description = models.TextField(max_length=100000, default='asdff')

    price = models.IntegerField(default='10000')

    image = models.ImageField(upload_to='img/', verbose_name='My Photo', default='iherbItems/img/banner/banner-1.jpg')

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(
        max_length=255,
        help_text="Username"
    )
    password = models.CharField(
        max_length=255,
        help_text="Username"
    )


class ItemEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Item):
            # Convert the Item object to a dictionary with all the field values
            return {
                'title': obj.title,
                'factory': obj.factory,
                'expiration_date': obj.expiration_date,
                'available_date': obj.available_date,
                'weight': obj.weight,
                'codeNumber': obj.codeNumber,
                'upcNumber': obj.upcNumber,
                'quantity': obj.quantity,
                'size': obj.size,
                'category': obj.category,
                'description': obj.description,
                'price': obj.price,
                'image': obj.image.url if obj.image else None,
            }
        return super().default(obj)
