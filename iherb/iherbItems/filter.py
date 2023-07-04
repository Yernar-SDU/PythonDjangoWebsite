from django import template

register = template.Library()


@register.filter
def categoryBestseller(items):
    bestsellers = []

    for item in items:
        if item.category == 'Bestseller':
            bestsellers.append(item)
    return bestsellers
