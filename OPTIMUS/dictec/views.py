from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group, GroupManager
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from datetime import datetime

# Create your views here.



def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('dashboard')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password no coninciden'
        })

def home(request):
    return render(request,'home.html')
   
def dashboard(request):
    return render(request,'dashboard.html')

def dashboard_docente(request):
    return render(request,'dashboard_docente.html')

def dashboard_estudiante(request):
    return render(request,'dashboard_estudiante.html')
       
 

def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password']
        )
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o Password es Incorecto'
        })

        else:
            login(request, user)
            data = user.groups.all()
            for g in data:
                print(g.name)
                if g.name=='administrativo':
                   return redirect('dashboard')
                elif g.name=='docentes':
                   return redirect('dashboard_docente')
                elif g.name=='estudiantes':
                   return redirect('dashboard_estudiante')
                else:
                    return redirect('home')
        
       