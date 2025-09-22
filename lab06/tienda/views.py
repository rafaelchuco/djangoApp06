from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria, 

def index(request):
    productos = Producto.objects.select_related('categoria').order_by('-pub_date')
    return render(request, 'tienda/index.html', {'productos': productos})

def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'tienda/producto.html', {'producto': producto})

def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    productos = categoria.productos.order_by('-pub_date')
    return render(request, 'tienda/categoria.html', {
        'categoria': categoria,
        'productos': productos
    })
