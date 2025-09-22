#!/usr/bin/env python
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab06.settings')
django.setup()

from django.contrib.auth.models import User

# Crear superusuario si no existe
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'Tecsup2023')
    print("✓ Superusuario 'admin' creado con password 'Tecsup2023'")
else:
    print("✓ Superusuario 'admin' ya existe")