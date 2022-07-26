from django.forms import ModelForm
from .models import Items
from .models import Weakness


class ItemsForm(ModelForm):
    class Meta:
        model= Items
        fields = ["name", "type"]
        
class WeaknessForm(ModelForm):
    class Meta:
        model = Weakness
        fields = ["name"]
