from django.contrib import admin
from .models import Proveedores, Productos

# admin.py en la carpeta Semana18App
 # Importa tus modelos aquí

admin.site.register(Proveedores)  # Registra el modelo Proveedores en el panel de administrador
admin.site.register(Productos)    # Registra el modelo Productos en el panel de administrador


# Register your models here.
