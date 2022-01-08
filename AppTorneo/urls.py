from django.urls import path 

from AppTorneo import views


urlpatterns = [

    path ('Inicio', views.inicio, name = "Inicio"),

    path ('Presentacion', views.presentacion, name = "Presentacion"),

    path ('Torneos', views.torneos, name = "Torneos"),

    path ('Equipos', views.equipos, name = "Equipos"),

    path ('Sedes', views.sedes, name = "Sedes"),

    path ('torneosFormulario', views.torneosFormulario, name="TorneosFormulario"),
        
    path ('buscar/', views.buscar),


    
] 