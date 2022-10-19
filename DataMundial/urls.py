from turtle import home
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path,include
from DataMundial.views import *


from . import views
from django.urls import include, re_path, path
#from django.conf.urls import url

# app_name = "chat"

urlpatterns = [
    path('', inicio),
    path('DataMundial/', inicio),
    path('inicio/', inicio),
    path('inicio2/', inicio2),
   
    path('selecciones/', ver_selecciones),
    path('grupos/', ver_grupos),
    path('login/', login_request),
    path('registro/', registro),
    path('perfil/editarPerfil/', editarPerfil),
    path('perfil/changepass/', changePass),
    path('logout/', LogoutView.as_view(template_name='inicio.html')),
    #path('concurso/', blog_concurso),
    path('miSeleccion/', miSeleccion),
    path('perfil/changeAvatar', AgregarAvatar),
    path('pronostico/', pronostico),    
    path('seleccionElegida/<seleccion_seleccion>', detalle_seleccion),
    
    re_path(r'concurso/', views.blog_concurso, name='form'),
    path('pronostico_blank/',views.pronostico_blank, name='pronostico_blank'),
    path('acercade/', acercade),
    path('ranking/', ranking),
    path('enviamsj/', enviamsj),
    # path("inicio/", views.inicio, name="inicio"),
    # path("<str:room_name>/", views.room, name="room")
    
]