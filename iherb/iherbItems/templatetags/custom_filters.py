from django import template


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

@register.filter
def categoryBestseller(items):
    bestsellers = []

    for item in items:
        if item.category == 'Bestseller':
            bestsellers.append(item)
    return bestsellers


@register.filter
def categoryNew(items):
    bestsellers = []

    for item in items:
        if item.category == 'New':
            bestsellers.append(item)
    return bestsellers

@register.filter
def categoryRecommended(items):
    bestsellers = []
    for item in items:
        if item.category == 'Recommended':
            bestsellers.append(item)
    return bestsellers
