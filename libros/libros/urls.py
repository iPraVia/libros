"""libros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import logout_then_login
from app import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/',v.login,name='login'),
    path('registro/',v.registro,name='registro'),
    path('catalogo/',v.catalogo,name='catalogo'),
    path('agregar/<int:libro_id>/', v.agregarLibro, name="agregarLibro"),
    path('limpiar/', v.limpiarCarrito, name="CLS"),
    path('restar/<int:libro_id>/', v.restarLibro, name="restar"),
    path('carrito/',v.carrito,name='carrito'),
    path('publicarLibro/',v.publicarLibro,name='publicarLibro'),
    path('logout/',logout_then_login,name='logout'),
    path('editarPerfil',v.editarPerfil,name='editarPerfil')
]
