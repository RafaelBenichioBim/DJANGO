from django.shortcuts import render
from .models import Produto

import ifcopenshell



def index(request):
    produtos = Produto.objects.all()

    ifc_file1 = ifcopenshell.open("C:/Users/Usuario/Desktop/REALIZA 1.ifc")
    lista = [objeto for objeto in ifc_file1.by_type('IfcElement')]

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!',
        'produtos': produtos,
        'lista': lista
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):

    prod = Produto.objects.get(id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)
