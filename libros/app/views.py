from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def inicio(request):
    return render(request, 'inicio.html')

def registro(request):
    return render(request, 'registro.html')

def catalogo(request):
    return render(request, 'catalogo.html')