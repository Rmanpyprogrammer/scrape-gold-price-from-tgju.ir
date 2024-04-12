 
from django.contrib import admin
from django.urls import path

urlpatterns = [
#scrap
path("api-gold/", Price_online_get, name="get-price"),
]
 

