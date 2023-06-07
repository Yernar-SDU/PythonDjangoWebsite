from django import template
from ..models import Item


register = template.Library()


@register.filter
def filter_by_category(items, category):
    result = []
    if category is None:
        return items
    for item in items:
        if item.category == category:
            result.append(item)
    return result