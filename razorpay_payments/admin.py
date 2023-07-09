from django.contrib import admin
from .models import *

@admin.register(Coffee)
class CoffeeDisplay(admin.ModelAdmin):
    list_display = ('name', 'amount', 'order_id', 'paid', )