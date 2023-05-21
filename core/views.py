from django.shortcuts import render,redirect
from .models import * 
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator

#listar productos
def index(request):
    productosAll = Producto.objects.all()
    page = request.GET.get('page', 1) # OBTENEMOS LA VARIABLE DE LA URL, SI NO EXISTE NADA DEVUELVE 1

    try:
        paginator = Paginator(productosAll, 2)#cantidad de productos
        productosAll = paginator.page(page)
    except:
        raise Http404

    data = {
        'lp': productosAll,
        'paginator': paginator
    }
    return render(request, 'core/index.html', data)


def blogdetails(request): 
    return render(request, 'core/blog-details.html')

def blog(request):
    return render(request, 'core/blog.html')

def checkout(request):
    return render(request,'core/checkout.html')

def main(request):
    return render(request, 'core/main.html')

def contact(request):
    return render(request, 'core/contact.html')


def shopdetails(request):
    return render(request, 'core/shop-details.html')

def shopgrid(request):
    return render(request, 'core/shop-grid.html')

def shopingcart(request):
    return render(request, 'core/shoping-cart.html')

def administrador(request):
    return render(request, 'core/administrador.html')

def administradorproducto(request):
    productosListados = Producto.objects.all()
    return render(request, 'core/administrador-producto.html',{"listado":productosListados})

def administradorcorreo(request):
    empleadoListados = Empleado.objects.all()
    return render(request, 'core/administrador-correo.html',{"listadoemp":empleadoListados})


#CRUD
def add(request):
    data = {
        'form' : ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Almacenado Correctamente")

    return render(request, 'core/add-product.html', data)

def update(request,id):
    producto = Producto.objects.get(id=id)
    data = {
        'form' : ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Actualizado Correctamente")
        data['form'] = formulario
    
    return render(request, 'core/update-product.html', data)
    
    
def delete(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect(to="index")


def add(request):
    data = {
        'form' : ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Almacenado Correctamente")

    return render(request, 'core/add-product.html', data)

def update(request,id):
    producto = Producto.objects.get(id=id)
    data = {
        'form' : ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Actualizado Correctamente")
        data['form'] = formulario
    
    return render(request, 'core/update-product.html', data)
    
    
def delete(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect(to="index")
