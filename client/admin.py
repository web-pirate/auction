from django.contrib import admin
from .models import *

# Register your models here.


class ItemFilter(admin.ModelAdmin):
    list_display = ('name', 'price', 'created', 'category')


class UserFilter(admin.ModelAdmin):
    list_display = ('user', 'dob', 'phone', 'address')


class BidFilter(admin.ModelAdmin):
    list_display = ('product', 'name', 'amout')


admin.site.register(Item, ItemFilter)
admin.site.register(UserDetails, UserFilter)
admin.site.register(Bid, BidFilter)
