from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'index.html')

def fuser(request):
    leitores = Usuario.objects.all()
    return render(request, 'foruser.html', {'leitores' : leitores})

def caduser(request):
    vnome = request.POST.get('nome')
    vemail = request.POST.get('email')

    if not vnome:
        return render(request, 'caduser.html', {'erro' : 'O nome é obrigatório.'})

    if not vemail:
        return render(request, 'caduser.html', {'erro' : 'O email é obrigatório.'})

    try:
        validate_email(vemail)
    except ValidationError:
        return render(request, 'caduser.html', {'erro' : 'O emial é obrigatório.'})

    Usuario.objects.create(nome=vnome, email=vemail)

    return render(request, 'caduser.html', {'sucesso!' : 'Foi cadastrado com sucesso.'})
