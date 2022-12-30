from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User




def login(request):
    if request.method != 'POST':
        return render(request, 'login.html')

    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=email, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos!')
        return render(request, 'login.html')
    else:
        auth.login(request, user)
        return redirect('dashboard')

def logout(request):
    auth.logout(request)
    return redirect('login')

def cadastro(request):
    if request.method!='POST':
        return render(request, 'cadastro.html')

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    repetirSenha = request.POST.get('repetirSenha')

    if not nome or not email or not senha or not repetirSenha:
        messages.error(request, 'Atenção, todos os campos devem ser preenchidos')
        return render(request, 'cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')    
        return render(request, 'cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'A senha precisa ter mais de 6 cáracteres')
        return render(request, 'cadastro.html')

    if repetirSenha != senha:
        messages.error(request, 'As senhas devem ser as mesmas!')
        return render(request, 'cadastro.html')

    if User.objects.filter(username=email).exists():
        messages.error(request, 'O email informado já foi cadastrado')
        return render(request, 'cadastro.html')

    user = User.objects.create_user(username=email, email=email, password=senha, first_name=nome)
    user.save()

    messages.success(request, 'Registrado com sucesso')
    return redirect('login')

