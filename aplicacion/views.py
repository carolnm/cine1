from django.shortcuts import render, redirect
from .models import Pelicula
from .forms import peliculaForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate


# Create your views here.
def home(request):
    data ={
        'peliculas': Pelicula.objects.all()
    }
    return render(request, "aplicacion/home.html", data)

def servicio(request):
    return render(request, "aplicacion/servicios.html")

def index(request):
    return render(request, "aplicacion/index.html")

def listar_pelicula(request):
    peliculas = Pelicula.objects.all()
    data = {
        'peliculas':peliculas
    } 

    return render (request, "aplicacion/listado_peliculas.html", data)    

@permission_required('aplicacion.add_pelicula')
def resgistrar_pelicula(request):
    data = {
        'form':peliculaForm() 
    }
    if request.method == 'POST':
        formulario = peliculaForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"

    return render(request, "aplicacion/registrar_pelicula.html", data)

def modificar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)

    data= {
        'form':peliculaForm(instance=pelicula)
    }
    if request.method == 'POST':
        formulario = peliculaForm(data=request.POST, instance=pelicula, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "modificado correctamente"
            data ['form'] = peliculaForm(instance=Pelicula.objects.get(id=id))
    return render(request, "aplicacion/modificar_pelicula.html", data)

def eliminar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()

    return redirect(to="listar_peli")     

def registrar_usuario(request):
    data = {
        'form': CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autentificar al usuario y redirigirlo al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')

    return render(request, 'registration/registrar.html', data)