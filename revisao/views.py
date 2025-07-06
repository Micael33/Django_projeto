from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def criar_conta(request):
    return render(request, 'cadastro.html')


