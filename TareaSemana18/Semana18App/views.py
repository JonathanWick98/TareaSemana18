from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from .Formularios.forms import ProveedorForm, NewUserForm, ProductoForm
from .models import Proveedores, Productos
from django.contrib.auth.decorators import user_passes_test

def reg_user(request):
    if request.method == "POST":
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = NewUserForm()

    return render(request, "Reg_user.html", {"form": formulario})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Cambiado a 'home' en lugar de 'index'
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def index(request):
    es_estudiante = request.user.groups.filter(name='Estudiante').exists()
    es_admin = request.user.is_staff

    if es_estudiante or es_admin:
        return render(request, 'index.html', {'user': request.user, 'es_estudiante': es_estudiante, 'es_admin': es_admin})
    else:
        return render(request, 'index.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def mostrar_proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'mostrar_proveedores.html', {'proveedores': proveedores})

@user_passes_test(lambda u: u.is_staff, login_url='denegado')
def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'agregar_proveedor.html', {'form': form})

class ProveedorListView(ListView):
    model = Proveedores
    template_name = 'mostrar_proveedores.html'
    context_object_name = 'proveedores'

class AgregarProveedorView(CreateView):
    model = Proveedores
    form_class = ProveedorForm
    template_name = 'agregar_proveedor.html'
    success_url = '/mostrar_proveedores/'

def mostrar_productos(request):
    productos = Productos.objects.all()
    return render(request, 'mostrar_productos.html', {'productos': productos})

@user_passes_test(lambda u: u.is_staff, login_url='denegado')
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_productos')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def denegado(request):
    return render(request, 'denegado.html')