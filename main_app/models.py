from django.db import models
from django.urls import reverse 

ITEM = (
    ("Berry 1","Aguav Berry"),
    ("Berry 2","Apicot Berry"),
    ("Berry 3","Aspear Berry"),
    ("Berry 4"," Babiri Berry"),
    ("Berry 5","Charti Berry"),
    ("Berry 6","Chesto Berry"),
    ("Berry 7","Chilan Berry"),
    ("Berry 8","Chople Berry"),
    ("Berry 9","Colbur Berry"),
    ("Berry 10","Custap Berry"),
    ("Berry 11","Enigma Berry"),
    ("Berry 12","Ganlon Berry"),
    ("Berry 13","Golden Golden Nanab Berry"),
    ("Berry 14","Golden Golden Pinap Berry"),
    ("Berry 15","Golden Razz Berry"),
    ("Berry 16","Hondew Berry"),
    ("Berry 17","Iapapa Berry"),
    ("Berry 18","Iapapa Berry"),
    ("Berry 19","Jaboca Berry"),
    ("Berry 20","Lansat Berry"),
    ("Berry 21","Liechi Berry"),
    ("Berry 22","Maranga Berry"),
    ("Berry 23","Pamtre Berry"),
    ("Berry 24","Payapa Berry"),
    ("Berry 25","Kelpsy Berry"),
    )

TYPE = (
    ("Type 1","Medicine"),
    ("Type 2","Battle Item"),
    ("Type 3","General Item"),
    ("Type 4"," Hold Item"),
    ("Type 5"," Machine"),
    ("Type 6","Artifact"),
)
 

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    moves = models.CharField(max_length=50)
    item = models.CharField(max_length=20)
    #weakness = models.ManyToManyField(Weakness)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

class Items(models.Model):
  type = models.CharField(
         max_length=50,
         choices=TYPE,
         default=TYPE[0][0]
                        
                        )
  name = models.CharField(
      max_length=50,
      choices=ITEM,
      default=ITEM[0][0]
  )
    
  def __str__(self):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    return f'{self.item_display()} on {self.type}'

class Weakness(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=20)
  
  def __str__(self):
    return self.name


class Moves(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=50)
  
  def __str__(self):
    return self.name