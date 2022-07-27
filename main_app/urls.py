from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('welcome/', views.welcome,name= 'welcome'),
    path('pokedex/', views.pokedex_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'), 
    path('pokedex/<int:Pokemon_id>/', views.pokedex_detail, name='detail'),
    path('pokedex/create', views.PokemonCreate.as_view(), name='Pokemon_create'),
    path('pokedex/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon_update'),
    path('pokedex/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon_delete'),
    path('pokedex/<int:Pokemon_id>/add_items/', views.add_items, name='add_items'),
    path('pokedex/<int:Pokemon_id>/add_weakness/', views.add_weakness, name='add_weakness'),
    path('pokedex/<int:Pokemon_id>/add_photo/', views.add_photo, name='add_photo')  
]