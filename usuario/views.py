from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

def home(request):
    return render(request, 'index.html')

def telacad(request):
    return render(request, 'telalog.html')

def fuser(request):
    usuarios = Usuario.objects.all()
    return render(request, 'foruser.html', {'usuarios' : usuarios})

def caduser(request):
    if request.method == "POST":
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
            return render(request, 'caduser.html', {'erro' : 'O email é inválido.'})

        try:
            Usuario.objects.create_user(username=vnome, email=vemail, password=vsenha)
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('fuser')
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar usuário: {str(e)}')
            return render(request, 'caduser.html')

    return render(request, 'caduser.html')

def updateuser(request, id):
    if request.method == "POST":
        vname = request.POST.get('username')
        vemail = request.POST.get('email')
        vsenha = request.POST.get('password')
        upusers = Usuario.objects.all(id=id)

        if not vname or not vemail or not vsenha:
            return render(request, 'updateuser.html', {'erro:' : 'Todos campos são obrigatórios!'})

        upusers.username = vname
        upusers.email = vemail
        upusers.password = vsenha
        Usuario.save()
        messages.success("Usuário salco com sucesso!")
        return redirect(fuser)

    return render(request, 'updateuser.html')

def loginuser(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        senha = request.POST['password']
        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            login(request, user)
            return redirect('telacad')

        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'login.html', {'erro': 'Usuário ou senha invalido'})

    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('login')