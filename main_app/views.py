from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Pokemon, Photo, Weakness, Items
import uuid
import boto3 
from .forms import ItemsForm
from .forms import WeaknessForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'pokedex-oa'

def home (request):
    return render(request, 'registration/login.html')


@login_required 
def pokedex_index(request):
    pokedex= Pokemon.objects.all()
    return render(request, 'pokedex/index.html',{'pokedex': pokedex})

@login_required 
def pokedex_detail(request, Pokemon_id):
    pokemon = Pokemon.objects.get(id=Pokemon_id)
    items_form = ItemsForm()
    weakness_form = WeaknessForm()
    return render(request, 'pokedex/detail.html',{'pokemon': pokemon,
    'items_form': items_form, 'weakness_form': weakness_form
    
    })
@login_required    
def add_items(request, pokemon_id):
  form = ItemsForm(request.POST)
 
  if form.is_valid():
    new_items = form.save(commit=False)
    new_items.pokemon_id = pokemon_id
    new_items.save()
  return redirect('detail', pokemon_id=pokemon_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
   
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def add_photo(request, pokemon_id):
    photo_file = request.FILES.get('photo-file',None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            
            photo = Photo(url=url, pokemon_id=pokemon_id)
            photo.save()
        except:
            print('An error occured uploading to S3')
    return redirect ('detail', pokemon_id= pokemon_id) 
        


class PokemonCreate(LoginRequiredMixin,CreateView):
    model = Pokemon
    fields = "__all__"
    success_url = '/pokedex/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)
    
class PokemonUpdate(LoginRequiredMixin,UpdateView):
    model = Pokemon
    fields = "__all__"
    success_url = '/pokedex/'

class PokemonDelete(LoginRequiredMixin,DeleteView):
    model = Pokemon
    fields = "__all__"
    success_url = '/pokedex/'