from django.forms import ModelForm
from .models import Items
from .models import Weakness
from django import forms
from django.contrib.auth.forms import UserCreationForm



class ItemsForm(ModelForm):
    class Meta:
        model= Items
        fields = ["name", "type"]
        
class WeaknessForm(ModelForm):
    class Meta:
        model = Weakness
        fields = ["name"]
