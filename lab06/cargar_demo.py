#!/usr/bin/env python
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab06.settings')
django.setup()

from tienda.models import Categoria, Producto

# Datos según la tabla del enunciado
data = {
    "Gaseosas": [("Fanta 500ml", 1.80, 10), ("Coca Cola 500ml", 2.50, 10), ("7up 500ml", 1.70, 10)],
    "Snacks": [("Cheetos", 1.00, 12), ("Chizito", 1.00, 12)],
    "Galletas": [("Picaras", 1.00, 12), ("Coronita Fresa", 0.70, 12)],
    "Chocolates": [("Princesa", 1.50, 8), ("Sublime", 1.50, 8), ("Triángulo", 1.20, 8)],
}

print("Cargando datos de demo...")

for cat_nombre, productos in data.items():
    cat, created = Categoria.objects.get_or_create(nombre=cat_nombre)
    if created:
        print(f"✓ Categoría '{cat_nombre}' creada")
    else:
        print(f"✓ Categoría '{cat_nombre}' ya existe")
    
    for nombre, precio, stock in productos:
        producto, created = Producto.objects.get_or_create(
            nombre=nombre, categoria=cat,
            defaults={'precio': precio, 'stock': stock}
        )
        if created:
            print(f"  ✓ Producto '{nombre}' creado - S/ {precio} - Stock: {stock}")
        else:
            print(f"  ✓ Producto '{nombre}' ya existe")

print("\n✅ ¡Datos de demo cargados exitosamente!")
print("\nPuedes:")
print("1. Ejecutar el servidor: python manage.py runserver")
print("2. Acceder al admin: http://127.0.0.1:8000/admin (admin/Tecsup2023)")
print("3. Ver la tienda: http://127.0.0.1:8000/")