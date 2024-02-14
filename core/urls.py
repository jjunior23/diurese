from django.contrib import admin
from django.urls import path
from .views import home, lista_diurese, diurese_novo, diurese_update, api_diurese

urlpatterns = [
    path('home/', home, name='home'),
    path('home', home, name='home'),
    path('lista_diurese', lista_diurese, name='lista_diurese'),
    path('diurese_novo', diurese_novo, name='diurese_novo'),
    path('diurese_update/<int:id>', diurese_update, name='diurese_update'),
    path('api/diurese/', api_diurese, name='api_diurese'),
    #path('funcao_delete/<int:id>', funcao_delete, name='funcao_delete'),

]