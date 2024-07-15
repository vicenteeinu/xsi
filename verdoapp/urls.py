from django.urls import path, include
from . import views

urlpatterns = [
    path('Vista_inicio', views.index, name='Vista_inicio'),
    path('login/', views.login, name='login'),
    path('usuarios_listar/', views.crud, name='usuarios_listar'),
    path('registro/', views.registro, name='registro'),
    path('home', views.home, name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('semillas/',views.semillas,name='semillas'),
    path('tierra/',views.tierra,name='tierra'),
    path('herramientas/',views.herramientas,name='herramientas'),
    path('maceteros/',views.maceteros,name='maceteros'),
]
