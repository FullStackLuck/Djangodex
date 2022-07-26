from django.contrib import admin

from .models import Items, Pokemon, Photo 

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Items)
admin.site.register(Photo)