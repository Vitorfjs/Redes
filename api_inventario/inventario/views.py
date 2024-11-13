from django.shortcuts import render
from .models import ItemInventario

def listar_itens(request):
    itens = ItemInventario.objects.all()
    return render(request, 'inventario/lista.html', {'itens': itens})
