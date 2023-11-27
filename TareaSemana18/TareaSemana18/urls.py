"""
URL configuration for TareaSemana18 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Semana18App import views as TareaApp18
from django.views.generic import RedirectView
from Semana18App.Formularios.forms import ProveedorForm
from Semana18App.views import ProveedorListView, AgregarProveedorView, mostrar_productos, agregar_producto

urlpatterns = [
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('registro/', TareaApp18.reg_user, name="registro"),
    path('login/', TareaApp18.iniciar_sesion, name="login"),
    path('logout/', TareaApp18.cerrar_sesion, name='logout'),
    path('home/', TareaApp18.index, name="home"),
    path('admin/', admin.site.urls),
    path('mostrar_proveedores/', TareaApp18.mostrar_proveedores, name='mostrar_proveedores'),
    path('agregar_proveedor/', TareaApp18.agregar_proveedor, name='agregar_proveedor'),
    path('mostrar_proveedores/', ProveedorListView.as_view(), name='mostrar_proveedores'),
    path('agregar_proveedor/', AgregarProveedorView.as_view(), name='agregar_proveedor'),
    path('mostrar_productos/', mostrar_productos, name='mostrar_productos'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('agregar_proveedor/', TareaApp18.agregar_proveedor, name='agregar_proveedor'),
    path('agregar_producto/', TareaApp18.agregar_producto, name='agregar_producto'),
    path('denegado/', TareaApp18.denegado, name='denegado'),
]
