#!/usr/bin/env python
import os
import django
import requests
from pathlib import Path

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab06.settings')
django.setup()

from tienda.models import Categoria, Producto

# URLs de imágenes reales para cada categoría
imagenes_categorias = {
    "Gaseosas": "https://images.unsplash.com/photo-1581006852262-e4307cf6283a?w=300&h=300&fit=crop&crop=center",
    "Snacks": "https://images.unsplash.com/photo-1599490659213-e2b9527bd087?w=300&h=300&fit=crop&crop=center", 
    "Galletas": "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=300&h=300&fit=crop&crop=center",
    "Chocolates": "https://images.unsplash.com/photo-1511381939415-e44015466834?w=300&h=300&fit=crop&crop=center"
}

# URLs de imágenes reales para cada producto
imagenes_productos = {
    "Fanta 500ml": "https://images.unsplash.com/photo-1624517452488-04869289c4ca?w=400&h=400&fit=crop&crop=center",
    "Coca Cola 500ml": "https://images.unsplash.com/photo-1554866585-cd94860890b7?w=400&h=400&fit=crop&crop=center",
    "7up 500ml": "https://images.unsplash.com/photo-1629203851122-3726ecdf5bd4?w=400&h=400&fit=crop&crop=center",
    "Cheetos": "https://images.unsplash.com/photo-1613919113640-25732ec5e61f?w=400&h=400&fit=crop&crop=center",
    "Chizito": "https://images.unsplash.com/photo-1613919113640-25732ec5e61f?w=400&h=400&fit=crop&crop=center",
    "Picaras": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&h=400&fit=crop&crop=center",
    "Coronita Fresa": "https://images.unsplash.com/photo-1549007994-cb92caebd54b?w=400&h=400&fit=crop&crop=center",
    "Princesa": "https://images.unsplash.com/photo-1511381939415-e44015466834?w=400&h=400&fit=crop&crop=center",
    "Sublime": "https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=400&h=400&fit=crop&crop=center",
    "Triángulo": "https://images.unsplash.com/photo-1571197219842-71d14f43e6e2?w=400&h=400&fit=crop&crop=center"
}

def descargar_imagen(url, ruta_destino):
    """Descarga una imagen desde una URL"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)
        
        with open(ruta_destino, 'wb') as archivo:
            for chunk in response.iter_content(chunk_size=8192):
                archivo.write(chunk)
        print(f"✅ Descargada: {ruta_destino}")
        return True
    except Exception as e:
        print(f"❌ Error descargando {url}: {e}")
        return False

def main():
    base_media = Path("media")
    
    print("🖼️ Descargando imágenes para categorías...")
    
    # Descargar imágenes de categorías
    for categoria in Categoria.objects.all():
        if categoria.nombre in imagenes_categorias:
            url = imagenes_categorias[categoria.nombre]
            nombre_archivo = f"{categoria.nombre.lower().replace(' ', '_')}.jpg"
            ruta_imagen = base_media / "categorias" / nombre_archivo
            
            if descargar_imagen(url, str(ruta_imagen)):
                # Actualizar el modelo con la ruta de la imagen
                categoria.foto = f"categorias/{nombre_archivo}"
                categoria.save()
                print(f"✅ Categoría '{categoria.nombre}' actualizada con imagen")
    
    print("\n🛍️ Descargando imágenes para productos...")
    
    # Descargar imágenes de productos
    for producto in Producto.objects.all():
        if producto.nombre in imagenes_productos:
            url = imagenes_productos[producto.nombre]
            nombre_archivo = f"{producto.nombre.lower().replace(' ', '_').replace('.', '')}.jpg"
            ruta_imagen = base_media / "productos" / nombre_archivo
            
            if descargar_imagen(url, str(ruta_imagen)):
                # Actualizar el modelo con la ruta de la imagen
                producto.imagen = f"productos/{nombre_archivo}"
                producto.save()
                print(f"✅ Producto '{producto.nombre}' actualizado con imagen")
    
    print("\n🎉 ¡Proceso completado! Todas las imágenes han sido descargadas y asignadas.")
    print("🌐 Refresca la página web para ver los cambios.")

if __name__ == "__main__":
    main()