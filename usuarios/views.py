from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

@login_required
def pagina1(request):
    return render(request, 'pag1.html')

@login_required
def pagina2(request):
    return render(request, 'pag2.html')

def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('senha')
    else:
        return render(request, 'cadastro.html')
    
def logout(request):
    logout(request)