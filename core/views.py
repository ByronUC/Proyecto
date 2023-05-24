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
        paginator = Paginator(productosAll, 3 )#cantidad de productos
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

def admproducto(request):
    productosListados = Producto.objects.all()
    return render(request, 'core/adm-producto.html',{"listado":productosListados})

def admcorreo(request):
    empleadoListados = Empleado.objects.all()
    return render(request, 'core/adm-correo.html',{"listadoemp":empleadoListados})

def registro(request):
    return render(request,'core/registro.html')


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
    return redirect("admproducto")


#CRUD Empleado

def addEmp(request):
    data = {
        'form': EmpleadoForm()
    }
    
    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Correo almacenado correctamente")
            return redirect('admcorreo')

    return render(request, 'core/add-correo.html', data)

def updateEmp(request, id):
    empleado = Empleado.objects.get(id=id)
    data = {
        'form': EmpleadoForm(instance=empleado)
    }
    
    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST, instance=empleado, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Correo actualizado correctamente")
            return redirect('admcorreo')
        data['form'] = formulario
    
    return render(request, 'core/update-correo.html', data)
    
    
def deleteEmp(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    messages.success(request, "Correo eliminado correctamente")
    return redirect('admcorreo')
 
def  cart(request,slug):
    product= Producto.objects.get(slug=slug)

    initial = {"item":[],"price":00, "count":00}
    session=request.session.get("data",initial)
    if slug in session["items"]:
        messages.error(request, "Producto ya existe en el carrito")
    else:
        session ["items"].append(slug)
        session ["price"] += float(Producto.precio)
        session ["count"] +=1
        request.session["data"]=session
        messages.success(request, "Agregado Exitosamente")
    return redirect("core:detail", slug)

