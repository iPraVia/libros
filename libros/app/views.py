from django.shortcuts import render
from django.db.models import Q
from app import models
from app import formularios

# Create your views here.
def index(request):
    form = formularios.IniciarSesion()
    if request.method == 'POST':
        form = formularios.IniciarSesion(request.POST)
        email = form['email'].value()
        password = form['password'].value()
        if models.Usuario.objects.filter(Q(email = email) & Q(password = password)).__len__() == 1 :
            usuario = models.Usuario.objects.get(Q(email = email) & Q(password = password))
            print("Nombre\n---> ",usuario.nombre)
            datos = {'usuario':usuario}
            return render(request,'inicio.html',datos)

    
        
    datos = {'form':form}
    return render(request,'index.html',datos)

def inicio(request):
    return render(request, 'inicio.html')

def crearUsuario(formulario):
    usuario = models.Usuario()
    usuario.nombre = formulario.cleaned_data['nombre']
    usuario.apellido = formulario.cleaned_data['apellido']
    usuario.rut = formulario.cleaned_data['rut']
    usuario.celular = formulario.cleaned_data['celular']
    usuario.email = formulario.cleaned_data['email']
    usuario.password = formulario.cleaned_data['password']
    usuario.terminos = formulario.cleaned_data['terminos']
    usuario.save()

def registro(request):
    form = formularios.userRegistrationForm()
    data = {'form':form}
    return render(request, 'registro.html',data)


def validar(request):
    form = formularios.userRegistrationForm()
    if request.method == 'POST':
        form = formularios.userRegistrationForm(request.POST)
        if form.is_valid():
            if models.Usuario.objects.filter(email__icontains=form.cleaned_data['email']).__len__() == 0:
                crearUsuario(form)
                return render(request, 'inicio.html')
            else:
                print("Correo ingresado ya se encuentra registrado")
                data = {'form':form}
                return render(request, 'registro.html',data)
            



def catalogo(request):
    return render(request, 'catalogo.html')