from django.shortcuts import render, redirect
from gu.models import Expediente
from django.http import HttpResponse

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import no_auth_user, allowed_user

from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
import random

logged = False

def index(request):
    return render(request,"index.html",{'version':random.uniform(11,50),})

@no_auth_user
def logpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('/home/')
        else:
            messages.info(request,'Usuario o Contraseña no validos')
    return render(request,"login.html",{'version':random.uniform(10,50),})
        
@no_auth_user
def registpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST) 
        if form.is_valid():             
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Usuario '+user+' registrado.')
            return redirect('/login/')
        else:    
            messages.info(request,'Alguno de los campos ingresados no es válido')
            content = {'version':random.uniform(10,10),'form':form,}
            return redirect('/register/')
    else:
        return render(request,"register.html",{'version':random.uniform(10,50),})

@login_required(login_url='/login/') 
def home(request):
    return render(request,"home.html",{'version':random.uniform(11,50),})


@login_required(login_url='/login/')
def resultado(request):
    if request.GET['nmr']:
        exp = request.GET['nmr']
        expediente = Expediente.objects.filter(numero__icontains = exp)
        content = {'expedientes':expediente, 'expediente_buscado':exp,'version':random.uniform(10,50),}
        return render(request, "resultados.html", content)

    else:
        return HttpResponse('Numero de expediente no valido.')
        #return render(request,"invalid.html",{'expediente_buscado':request.GET['nmr']})

@login_required(login_url='/login/')
def busqueda(request):
    expediente = Expediente.objects.all()
    content = {'expedientes':expediente,'version':random.uniform(10,50),}
    return render(request,"busqueda.html",content)

@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return redirect('/login/')