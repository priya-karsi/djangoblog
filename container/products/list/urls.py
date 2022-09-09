from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home),
    path('show/',views.show,name='show'),
    path('addProduct/',views.addProduct,name='addProduct'),
    path('addData/',views.addData,name='addData'),
    path('edit/<pk>',views.edit,name='edit'),
    path('update',views.update,name='update'),
    path('delete/<pk>',views.delete,name='delete'),
]

