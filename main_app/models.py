from unicodedata import name
from django.db import models
from django.forms import CharField
from django.urls import reverse 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Come back and edit the items pokemon can home.

ITEM = (
    ("Berry 1","Aguav Berry"),
    ("Berry 2","Apicot Berry"),
    ("Berry 3","Aspear Berry"),
    ("Berry 4"," Babiri Berry"),
    ("Berry 5","Charti Berry"),
    ("Battle 6","XAttack"),
    ("Battle 7","Reset Urge"),
    ("Battle 8","Sassy Mint"),
    ("Battle 9","Relaxed Mint"),
    ("Battle 10","Guard Spec."),
    ("Battle 11","Brave Mint"),
    ("Hold 12","Black Belt"),
    ("Hold 13","Assualt Vest"),
    ("Hold 14","Air Ballon"),
    ("Hold 15","Absolite"),
    ("Machine 16","HM04"),
    ("Machine 17","HM03"),
    ("Machine 18","HM02"),
    ("Machine 19","HM01"),
    ("Machine 20","Lansat Berry"),
    ("Medicine 21","Clever Wing"),
    ("Medicine 22","Calcium"),
    ("Medicine 23","Burn Heal"),
    ("Medicine 24","Awakening"),
    ("Medicine 25","Antidote"),
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


WEAK = (
    ("Weakness 1","Normal"),
    ("Weakness 2","Fire"),
    ("Weakness 3","Water"),
    ("Weakness 4"," Electric"),
    ("Weakness 5","Grass"),
    ("Weakness 6","Ice"),
    ("Weakness 7","Fighting"),
    ("Weakness 8","Poison"),
    ("Weakness 9","Ground"),
    ("Weakness 10","Flying"),
    ("Weakness 11","Psychic"),
    ("Weakness 12","Bug"),
    ("Weakness 13","Rock"),
    ("Weakness 14","Ghost"),
    ("Weakness 15","Dragon"),
    ("Weakness 16","Dark"),
    ("Weakness 17","Steel"),
    ("Weakness 18","Fairy"), 
)

#Weakness has a ManytoMany Relationship with Pokemon
class Weakness(models.Model):
 name = models.CharField(
      max_length=20,
      choices=WEAK,
      default=WEAK[0][0])

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('weakness_detail', kwargs={'pk': self.id})

class Moves(models.Model):
    move1 = CharField(max_length=20)
    move2 = CharField(max_length=20)
    move3 = CharField(max_length=20)
    move4 = CharField(max_length=20)
    
def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('moves_detail', kwargs={'pk': self.id})
    
    
    

class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    attack = models.IntegerField(max_length=3)
    defense = models.IntegerField(max_length=3)
    specialatk = models.IntegerField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})



# Items has a OnetoMany Relationship with Pokemon
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
  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
  def __str__(self):
    return f'{self.get_name_display()} on {self.name}'


class Photo(models.Model):
    url= models.CharField(max_length=200)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Photo for pokemon_id:{self.pokemon_id} @{self.url}"




