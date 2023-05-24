from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('blogdetails/', blogdetails, name="blogdetails"),
    path('blog/', blog, name="blog"),
    path('checkout/', checkout, name="checkout"),
    path('main/', main, name="main"),
    path('contact/', contact, name="contact"),
    path('shopdetails/', shopdetails, name="shopdetails"),
    path('shopgrid/', shopgrid, name="shopgrid"),
    path('shopingcart/', shopingcart, name="shopingcart"),
    path('admproducto/', admproducto, name="admproducto"),
    path('admcorreo/', admcorreo, name="admcorreo"),
    path('administrador/',administrador, name="administrador"),
    path('registro/',registro, name="registro"),
    #CRUD

    path('add/' , add, name="add"),
    path('update/<id>/', update, name="update"),
    path('delete/<id>/', delete, name="delete"),

    #Crud Empleado

    path('addEmp/' , addEmp, name="addEmp"),
    path('updateEmp/<id>/', updateEmp, name="updateEmp"),
    path('deleteEmp/<id>/', deleteEmp, name="deleteEmp"),
]