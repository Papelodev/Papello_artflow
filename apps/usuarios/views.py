from django.shortcuts import render, redirect

from apps.usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from apps.usuarios.models import MyUser

from apps.customers.models import CustomerProfile

from django.contrib import auth, messages

import json


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            
        )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request,f"{nome} logado com sucesso")
                return redirect('meus_pedidos')
            else:
                messages.error(request,"Erro ao efetuar Login")
                return redirect('login')


    return render(request, "usuarios/login.html",{"form":form})

def cadastro(request):

    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

    if form.is_valid():
        
        
        nome=form["nome_cadastro"].value()
        email=form["email"].value()
        senha=form["senha_1"].value()
        userType=form["tipo_usuario"].value()

        if  MyUser.objects.filter(username=nome).exists():
            messages.error(request,"Usuário já existente")
            return redirect('cadastro')
        
        usuario = MyUser.objects.create_user(
            username=nome,
            email=email,
            password=senha,
            user_type=userType,
        )
        usuario.save()
        messages.success(request, "cadastro efetuado com sucesso")
        return redirect('login')


    return render(request, "usuarios/cadastro.html",{"form":form})

def logout(request):

    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')


def meus_dados(request):
    user = CustomerProfile.objects.get(user=request.user)
    print(user.address)
    return render(request, "usuarios/meus_dados.html", {'user': user})