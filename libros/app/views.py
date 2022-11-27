from django.shortcuts import redirect, render
from app import Carrito
from app.models import Libro
from django.shortcuts import render
from django.db.models import Q
from app import models
from app import formularios

# Create your views here.
def login(request):
    form = formularios.IniciarSesion()
    if request.method == 'POST':
        form = formularios.IniciarSesion(request.POST)
        email = form['email'].value()
        password = form['password'].value()
        if models.Usuario.objects.filter(Q(email = email) & Q(password = password)).__len__() == 1 :
            usuario = models.Usuario.objects.get(Q(email = email) & Q(password = password))
            print("Nombre\n---> ",usuario.nombre)
            datos = {'usuario':usuario}
            return render(request,'catalogo.html',datos)

    datos = {'form':form}
    return render(request,'login.html',datos)

def crearUsuario(request,formulario):
    form = formularios.IniciarSesion()
    usuario = models.Usuario()

    usuario.nombre = formulario.cleaned_data['nombre']
    usuario.apellido = formulario.cleaned_data['apellido']
    usuario.rut = formulario.cleaned_data['rut']
    usuario.celular = formulario.cleaned_data['celular']
    usuario.email = formulario.cleaned_data['email']
    usuario.password = formulario.cleaned_data['password']
    usuario.terminos = formulario.cleaned_data['terminos']
    usuario.estado = True

    usuario.save()
    datos = {'form':form}
    return render(request,'login.html',datos)

def registro(request):
    form = formularios.userRegistrationForm()
    formlogin = formularios.IniciarSesion()
    if request.method == 'POST':
        form = formularios.userRegistrationForm(request.POST)
        if form.is_valid():
            if models.Usuario.objects.filter(email__icontains=form.cleaned_data['email']).__len__() == 0:
                crearUsuario(request,form)
                return render(request,'login.html',{'form':formlogin})
            else:
                print("Correo ingresado ya se encuentra registrado")
                data = {'form':form}
                return render(request, 'registro.html',data)
    data = {'form':form}
    return render(request, 'registro.html',data)

            

def catalogo(request):
    libros = Libro.objects.all()  
    return render(request, 'catalogo.html', {'libros': libros})

def agregarLibro(request, libro_id):
    carrito = Carrito(request)
    producto = Libro.objects.get(id=libro_id)
    carrito.agregar(producto)
    return redirect("catalogoss")

