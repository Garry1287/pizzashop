from django.contrib import admin

# Register your models here.
from pizzashopapp.models import PizzaShop, Pizza

admin.site.register(PizzaShop)
admin.site.register(Pizza)
