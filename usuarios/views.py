from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login as login_django
from .models import CustomUser
from django.contrib import messages


def index(request):
    user = CustomUser.objects.all()
    context = {'user':user}
    return render(request, 'index.html', context)

@login_required
def pagina1(request):
    if request.user.is_authenticated:
        pass
    return render(request, 'pag1.html')

@login_required
def pagina2(request):
    return render(request, 'pag2.html')

def cadastro(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        data_nascimento = request.POST.get('data_nascimento')
        idade = request.POST.get('idade')

        user = CustomUser.objects.filter(username=username).first()

        if user:
            messages.error(request, 'Já existe um usuario com esse nome! Tente outro')

        novo_usario = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password,data_nascimento=data_nascimento, idade=idade)
        novo_usario.save()
        messages.success(request, 'Usuario cadastrado!')
        return redirect('registration/login')
    else:
        return render(request, 'cadastro.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return redirect('pag1')
    else:
        return render(request, 'login.html')


def logout(request):
    logout(request)
    return redirect('login')