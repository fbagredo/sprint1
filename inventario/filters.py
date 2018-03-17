from inventario.models import Producto, Proveedor
import django_filters
from django import forms

class ProductoFilter(django_filters.FilterSet):
    
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')
    tipoProducto = django_filters.CharFilter(lookup_expr='icontains')
    medidas = django_filters.CharFilter(lookup_expr='icontains')
    proveedor = django_filters.ModelMultipleChoiceFilter(queryset=Proveedor.objects.all(),
    widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'tipoProducto', 'medidas']