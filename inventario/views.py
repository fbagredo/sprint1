from inventario.models import Producto
from django.shortcuts import render
from .filters import ProductoFilter

def consultarProductos(request):
    producto_list = Producto.objects.all()
    producto_filter = ProductoFilter(request.GET, queryset=producto_list)
    return render(request, 'product_list.html', {'filter': producto_filter})