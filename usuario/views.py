from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

def home(request):
    return render(request, 'index.html')

def fuser(request):
    usuarios = Usuario.objects.all()
    return render(request, 'foruser.html', {'usuarios' : usuarios})

def caduser(request):
    vnome = request.POST.get('username')
    vsenha = request.POST.get('password')
    vemail = request.POST.get('email')

    if not vnome:
        return render(request, 'caduser.html', {'erro' : 'O nome é obrigatório.'})

    if not vsenha:
        return render( request, 'caduser.html', {'erro': 'A senhea é obrigatoria'})

    if not vemail:
        return render(request, 'caduser.html', {'erro' : 'O email é obrigatório.'})

    try:
        validate_email(vemail)
    except ValidationError:
        return render(request, 'caduser.html', {'erro' : 'O emial é inválido.'})

    Usuario.objects.create_user(username=vnome, email=vemail, password=vsenha)

    return render(request, 'caduser.html', {'sucesso!' : 'Foi cadastrado com sucesso.'})

def login(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, senha=senha)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'login.html', {'erro': 'Usuário ou senha invalido'})

def logout(request):
    logout(request)
    return redirect('login')