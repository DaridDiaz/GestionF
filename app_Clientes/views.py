from django.shortcuts import render

def clientes(request):


    ctx = {

    }

    return render(request, 'clientes/clientes.html', ctx)
