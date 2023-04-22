from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login as login_django
from .models import CustomUser
from django.contrib import messages

@login_required
def index(request):
    user = CustomUser.objects.all()
    context = {'user':user}
    return render(request, 'index.html', context)


#decorador que sinaliza que a pagina so pode ser acessada
#caso o usuario esteja logado
@login_required(login_url='/accounts/login/')
def pagina1(request):
    return render(request, 'pag1.html')

#decorador que sinaliza que a pagina so pode ser acessada
#caso o usuario esteja logado
@login_required(login_url='/accounts/login/')
def pagina2(request):
    return render(request, 'pag2.html')

def cadastro(request):
    #verifica se o metodo da requisição é igual a POST,
    #se for, ele obtem o valor de cada campo via template
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        data_nascimento = request.POST.get('data_nascimento')
        idade = request.POST.get('idade')

        #verifica se ja existe um usuario com esse mesmo nome
        user = CustomUser.objects.filter(username=username, email=email).first()

        #caso exista, ele irá exibir uma mensagem de erro no template
        if user:
            messages.error(request, 'Já existe um usuario com esse nome! Tente outro')

        #se o usuario não existir, ele irá criar um com os valores obtidos no template e salva-lo
        novo_usario = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password,data_nascimento=data_nascimento, idade=idade)
        novo_usario.save()
        messages.success(request, 'Usuario cadastrado!')
        return redirect('login')
    else:
        return render(request, 'cadastro.html')
    

def login(request):
    #verifica se o metodo da requisição é POST, se for, recebe o valor dos respectivos campos
    #do input no template
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #caso os valores do input sejam iguais ao de um usario cadastrado, ele o autentica
        user = authenticate(username=username, password=password)
        
        #caso existe um usuario com esse nome e senha, ele irá se logar e sera redirecionado para
        #a pagina a pagina 1
        if user:
            login_django(request, user)
            return redirect('home')
        else:
            #caso não exista esse usuario, será mostrado uma mensagem de erro no template
            messages.error(request, 'Essa pagina não existe')
    else:
        #retorna a renderização da pagina login, caso o metodo da requisição não seja POST
        return render(request, 'login.html')

def logout_django(request):
    #a função logout recebe uma request que desloga o usuario e o redireciona para uma pagina de login
    logout(request)
    return redirect('login')