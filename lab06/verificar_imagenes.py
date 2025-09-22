#!/usr/bin/env python
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab06.settings')
django.setup()

from tienda.models import Categoria, Producto

def main():
    print("📊 RESUMEN DE IMÁGENES:")
    print("=" * 50)
    
    # Mostrar estado de categorías
    print("\n📂 CATEGORÍAS:")
    for categoria in Categoria.objects.all():
        estado = "✅ Con imagen" if categoria.foto else "❌ Sin imagen"
        print(f"  - {categoria.nombre}: {estado}")
    
    # Mostrar estado de productos
    print("\n🛍️ PRODUCTOS:")
    for producto in Producto.objects.all():
        estado = "✅ Con imagen" if producto.imagen else "❌ Sin imagen"
        print(f"  - {producto.nombre}: {estado}")
    
    # Contar totales
    categorias_con_imagen = Categoria.objects.exclude(foto='').exclude(foto__isnull=True).count()
    total_categorias = Categoria.objects.count()
    
    productos_con_imagen = Producto.objects.exclude(imagen='').exclude(imagen__isnull=True).count()
    total_productos = Producto.objects.count()
    
    print(f"\n📈 ESTADÍSTICAS:")
    print(f"  Categorías con imagen: {categorias_con_imagen}/{total_categorias}")
    print(f"  Productos con imagen: {productos_con_imagen}/{total_productos}")
    
    if categorias_con_imagen == total_categorias and productos_con_imagen == total_productos:
        print("\n🎉 ¡Perfecto! Todos los elementos tienen imágenes.")
    else:
        print("\n⚠️ Algunos elementos aún necesitan imágenes.")

if __name__ == "__main__":
    main()