from django.contrib import admin
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock','descripcion','tipo']
    search_fields = ['nombre']
    list_per_page = 10
    list_editable = ['precio','stock','descripcion','tipo']
    list_filter = ['tipo','stock']

class EmpleadoAdmin (admin.ModelAdmin):
   list_display = ['nombreEmp','edad','rut','direccion','correo']
   search_fields = ['nombre']
   list_per_page = 10
   list_editable =['edad','rut','direccion','correo']
   

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombreCli','edad','rut','direccion','correo']
    search_fields = ['nombre']
    list_per_page = 10
    list_editable = ['edad','rut','direccion','correo']


class SubscripcionAdmin(admin.ModelAdmin):
    list_display = ['nombreSubs','correo','rut']
    search_fields = ['correo']
    list_per_page = 10
    list_editable = ['correo']      

admin.site.register(TiposProductos)
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Subscripcion,SubscripcionAdmin)


