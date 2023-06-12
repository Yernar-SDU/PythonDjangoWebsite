import json

from django.core.serializers import serialize
from django.db import models

from .models import Item


class FixedSizeStack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        if len(self.stack) >= self.max_size:
            self.stack.pop(0)
        self.stack.append(item)

    def get_items(self):
        return self.stack

    def clear(self):
        self.stack = []


RECENT_VIEWED_ITEMS_QUEUE = 'recent_viewed_items'


class DjangoModelEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, models.Model):
            return serialize('json', [obj])[1:-1]
        return super().default(obj)


default_items = Item.objects.first()