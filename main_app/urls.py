from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('main/', views.main, name= 'main'),
    path('pokedex/', views.pokedex_index, name='index'),
    path('pokedex/<int:Pokemon_id>/', views.pokedex_detail, name='detail'),
    path('pokedex/create', views.PokemonCreate.as_view(), name='Pokemon_create'),
    path('pokedex/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon_update'),
    path('pokedex/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon_delete'),
]