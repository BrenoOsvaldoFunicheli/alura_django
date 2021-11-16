
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id_receita>/', views.receita, name="receita"),
    path('request/', views.http_request, name="request"),
]
