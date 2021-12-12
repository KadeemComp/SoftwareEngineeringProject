from django.contrib import admin
from .models import Country, Fruit
# Register your models here.

admin.site.register(Fruit)
admin.site.register(Country)