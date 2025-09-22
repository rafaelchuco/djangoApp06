#!/usr/bin/env python
import os
import django
import requests
from pathlib import Path

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab06.settings')
django.setup()

from tienda.models import Producto

# URLs alternativas para productos faltantes
imagenes_faltantes = {
    "7up 500ml": "https://images.unsplash.com/photo-1547036967-23d11aacaee0?w=400&h=400&fit=crop&crop=center",
    "Princesa": "https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=400&h=400&fit=crop&crop=center",
    "Sublime": "https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=400&h=400&fit=crop&crop=center",
    "Triángulo": "https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=400&h=400&fit=crop&crop=center"
}

def descargar_imagen(url, ruta_destino):
    """Descarga una imagen desde una URL"""
    try:
        response = requests.get(url, stream=True, timeout=10)
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
    
    print("🛍️ Completando imágenes faltantes...")
    
    # Descargar imágenes de productos faltantes
    for producto in Producto.objects.filter(nombre__in=imagenes_faltantes.keys()):
        if not producto.imagen:  # Solo si no tiene imagen
            url = imagenes_faltantes[producto.nombre]
            nombre_archivo = f"{producto.nombre.lower().replace(' ', '_').replace('.', '')}.jpg"
            ruta_imagen = base_media / "productos" / nombre_archivo
            
            if descargar_imagen(url, str(ruta_imagen)):
                # Actualizar el modelo con la ruta de la imagen
                producto.imagen = f"productos/{nombre_archivo}"
                producto.save()
                print(f"✅ Producto '{producto.nombre}' actualizado con imagen")
    
    print("\n📊 Resumen de imágenes:")
    print("=" * 50)
    
    # Mostrar estado de categorías
    print("\n📂 CATEGORÍAS:")
    for categoria in django.db.models.query.Categoria.objects.all():
        estado = "✅ Con imagen" if categoria.foto else "❌ Sin imagen"
        print(f"  - {categoria.nombre}: {estado}")
    
    # Mostrar estado de productos
    print("\n🛍️ PRODUCTOS:")
    for producto in Producto.objects.all():
        estado = "✅ Con imagen" if producto.imagen else "❌ Sin imagen"
        print(f"  - {producto.nombre}: {estado}")
    
    print("\n🎉 ¡Proceso completado!")

if __name__ == "__main__":
    main()