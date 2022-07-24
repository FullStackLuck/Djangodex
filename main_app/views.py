from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Pokemon 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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