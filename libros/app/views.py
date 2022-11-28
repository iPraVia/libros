from django.shortcuts import redirect, render
from app.Carrito import Carrito

from app.models import Libro

# Create your views here.
def index(request):
    return render(request,'index.html')

def inicio(request):
    return render(request, 'inicio.html')

def registro(request):
    return render(request, 'registro.html')

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
