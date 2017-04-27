from django.contrib import admin
from .models import OnlineRetailer, UsAddress, Buyer, RMA, Return

# Register your models here.
"""
admin.site.register(OnlineRetailer)
admin.site.register(UsAddress)
admin.site.register(Buyer)
admin.site.register(RMA)
admin.site.register(Return)
"""

# Define the admin class


class RMAInline(admin.TabularInline):
    model = RMA


class BuyerInline(admin.TabularInline):
    model = Buyer


@admin.register(OnlineRetailer)
class OnlineRetailerAdmin(admin.ModelAdmin):
    list_display = ('name', 'web')
    inlines = [RMAInline]


@admin.register(UsAddress)
class UsAddressAdmin(admin.ModelAdmin):
    inlines = [BuyerInline]


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email',
                    'phone', 'address')
    inlines = [RMAInline]


@admin.register(RMA)
class RMAAdmin(admin.ModelAdmin):
    list_display = ('rma_number', 'retailer',
                    'order_number', 'order_date',
                    'brand', 'model',
                    'size', 'buyer')
    list_filter = ('retailer', 'order_date')


@admin.register(Return)
class ReturnAdmin(admin.ModelAdmin):
    list_display = ('user', 'initiate_date',
                    'retailer', 'order_number',
                    'brand', 'model',
                    'size', 'buyer')
