# from django import template
#
# from PythonDjangoWebsite.iherb.iherbItems.models import Item
#
# register = template.Library()
#
#
# @register.filter
# def categoryBestseller(items):
#     items = Item.objects.all()
#     bestsellers = []
#
#     for item in items:
#         if item.category == 'Bestseller':
#             bestsellers.append(item)
#     return bestsellers
