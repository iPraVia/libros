from django.shortcuts import redirect, render
from app.Carrito import Carrito

from app.models import Libro
from app.models import Genero
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q
from app import models
from app import formularios
from app import sumaTotal

from django.contrib import auth

def login(request):
    libros = Libro.objects.all()
    form = formularios.IniciarSesion()
    if request.method == 'POST':
        form = formularios.IniciarSesion(request.POST)
        username = form['email'].value()
        password = form['password'].value()
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None and user.is_active:
            print(username)
            auth.login(request, user)
            # Redirect to a success page.
            return redirect('catalogo')
        else:
            print("no entro")
            return redirect('login')
    datos = {'form':form,'libros':libros}
    return render(request,'login.html',datos)


def crearUsuario(formulario):
    usuario = models.Usuario()
    usuario.nombre = formulario.cleaned_data['nombre']
    usuario.apellido = formulario.cleaned_data['apellido']
    usuario.rut = formulario.cleaned_data['rut']
    usuario.celular = formulario.cleaned_data['celular']
    usuario.email = formulario.cleaned_data['email']
    usuario.password = formulario.cleaned_data['password']
    usuario.terminos = formulario.cleaned_data['terminos']
    usuario.estado = True

    user = User.objects.create_user(username=usuario.email,email=usuario.email,password=usuario.password,first_name=usuario.nombre,last_name=usuario.apellido,is_staff=False,is_active=True,is_superuser=False)
    user.save()
    usuario.save()

def registro(request):
    form = formularios.userRegistrationForm()
    if request.method == 'POST':
        form = formularios.userRegistrationForm(request.POST)
        if form.is_valid():
            if models.Usuario.objects.filter(email__icontains=form.cleaned_data['email']).__len__() == 0:
                crearUsuario(form)
                return redirect('login')
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
    libro = Libro.objects.get(id=libro_id)
    carrito.agregar(libro)
    return redirect("catalogo")

def limpiarCarrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("catalogo")

def restarLibro(request, libro_id):
    carrito = Carrito(request)
    libro = Libro.objects.get(id=libro_id)
    carrito.restar(libro)
    return redirect("catalogo")

def carrito(request):
    return render(request, 'carrito.html')

def publicarLibro(request):
    generos = Genero.objects.all()
    if request.method == 'POST':
        imagen = request.POST['urlImagen']
        titulo = request.POST['titulo']
        precio = request.POST['precio']
        comentario = request.POST['comentario']
        genero = request.POST['inputGenero']
        gen = Genero.objects.get(id=genero)
        usuario = User.objects.get(username=request.user.username)

        libro = Libro()
        libro.imagen = imagen
        libro.nombre = titulo
        libro.precio = precio
        libro.descripcion = comentario
        libro.usuario = usuario
        libro.genero = gen

        libro.save()
        return redirect("catalogo")
    return render(request,'publicarLibro.html',{'genero':generos})

def editarPerfil(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        password = request.POST['password']
        user = User.objects.get(username=request.user.username,password=request.user.password )
        user.first_name = nombre
        user.last_name = apellido
        user.save()
        return redirect('catalogo')
    return render(request,'editarPerfil.html')