from django.contrib import admin

from .models import Items, Pokemon

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Items)