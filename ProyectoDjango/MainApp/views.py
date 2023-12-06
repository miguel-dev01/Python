from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from MainApp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Importo el decorador en Django. Esto hará que se ejecute dicho decorador justo antes de que se ejecute otra función. EJ: Loguear...
# from django.contrib.auth.decorators import login_required

# Create your views here.

def Index(request):

    return render(request, 'mainapp/index.html',{
        'title': 'INICIO, del Index'
    })

def About(request):

    return render(request, 'mainapp/about.html',{
        'title': 'SOBRE NOSOTROS'
    })

def Register_Page(request):

    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Te has registrado correctamente')

            return redirect('Inicio')

    return render(request, 'users/register.html', {
        'title': 'Regístrese en el sistema',
        'registraco': register_form
    })

def Login_Page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('Inicio')
        else:
            messages.warning(request, 'Lo sentimos. No te has logueado correctamente')

    return render(request, 'users/login.html', {
        'title': 'Identifíquese al sistema:'
    })

def Logout_User(request):

    logout(request)

    return redirect('Loguear')