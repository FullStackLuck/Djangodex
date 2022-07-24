from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.



def home (request):
    return HttpResponse('<h1>Home Page</h1>')

def main (request):
    return render(request, 'welcome.html')

def pokedex_index(request):
    pokedex= Pokemon.objects.all()
    return render(request, 'pokedex/index.html',{'pokedex': pokedex})

def pokedex_detail(request, Pokemon_id):
    pokemon = Pokemon.objects.get(id=Pokemon_id)
    return render(request, 'pokedex/detail.html',{'pokemon': pokemon})




class PokemonCreate(CreateView):
    model = Pokemon
    fields = "__all__"
    success_url = '/pokedex/'
    
class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = "__all__"
    success_url = '/pokedex/'

class PokemonDelete(DeleteView):
    model = Pokemon
    fields = "__all__"
    success_url = '/pokedex/'