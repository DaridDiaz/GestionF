from django.shortcuts import render
from django.contrib import messages

def clientes(request):


    ctx = {

    }

    return render(request, 'clientes/clientes.html', ctx)

def deposito(request):


    ctx = {

    }

    return render(request, 'clientes/deposito.html', ctx)

def inicio(request):


    ctx = {

    }

    return render(request, 'clientes/inicio.html', ctx)

