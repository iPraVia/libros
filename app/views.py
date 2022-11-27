from django.shortcuts import redirect, render
from app import Carrito

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
    producto = Libro.objects.get(id=libro_id)
    carrito.agregar(producto)
    return redirect("catalogoss")

