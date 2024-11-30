from django.contrib import admin
from .models import Flavor, IceCreamType, Topping

# Registering models with the admin site
@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    list_display = ('id', 'flavor')  # Fields to display in the admin list view
    search_fields = ('flavor',)     # Enable search functionality


@admin.register(IceCreamType)
class IceCreamTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'price')  # Display fields
    search_fields = ('type',)              # Searchable fields
    list_filter = ('price',)               # Add filters for price


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')  # Display fields
    search_fields = ('name',)              # Searchable fields
    list_filter = ('price',)               # Add filters for price
