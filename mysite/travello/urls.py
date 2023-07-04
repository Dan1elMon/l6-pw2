from django.urls import path

from . import views

urlpatterns= [
    path("",views.index, name="index.html"),

    path('destinos/', views.destinos_list, name='destinos_list'),

    
] 