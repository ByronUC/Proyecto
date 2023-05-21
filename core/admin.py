from django.contrib import admin
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock','descripcion','tipo']
    search_fields = ['nombre']
    list_per_page = 10
    list_editable = ['precio','stock','descripcion','tipo']
    list_filter = ['tipo','stock']

#class EmpleadoAdmin (admin.ModelAdmin):
   #list_display = ['nombreEmp','edad','rut','direccion','correo']
   #search_fields = ['nombre']
    #list_per_page = 10
    #list_editable =['nombre','edad','rut','direccion','correo']
    #list_filter = ['rut']    

#class ClienteAdmin(admin.ModelAdmin):
    #list_display = ['nombreCli','edad','rut','direccion','correo']
    #search_fields = ['nombre']
    #list_per_page = 10
    #list_editable = ['nombreCli','edad','rut','direccion','correo']
    #list_filter = ['rut'] 

#class SubscripcionAdmin(admin.ModelAdmin):
    #list_display = ['correo']
    #search_fields = ['correo']
    #list_per_page = 10
    #list_editable = ['correo']
    #list_filter = ['correo']       

admin.site.register(TiposProductos)
#admin.site.register(Empleado,EmpleadoAdmin)
#admin.site.register(Cliente,ClienteAdmin)
#admin.site.register(Subscripcion,ProductoAdmin)
#admin.site.register(Producto,SubscripcionAdmin)

