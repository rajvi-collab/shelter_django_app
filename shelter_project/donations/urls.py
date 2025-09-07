"""Urls for donation application"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_report, name='inventory_list'),
    path('add/', views.add_donation, name='add_donation'),
    path('distribute/', views.distribute, name='distribute'),
    path('inventory/', views.inventory_report, name='inventory_list'),
    path('donors/', views.donor_report, name='donor_list'),
]
