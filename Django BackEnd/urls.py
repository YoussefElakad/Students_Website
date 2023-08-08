from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/',views.login,name="login"),
    path('home/',views.home,name="home"),
    path('Add student Page/',views.Add,name="Add"),
    path('Departement selection page/',views.Departement,name="Departement"),
    path('Edit Page/',views.Edit,name="Edit"),
    path('Search page/',views.Search,name="Search"),
    path('View Students Page/',views.View,name="View"),
]