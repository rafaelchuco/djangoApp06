from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    foto = models.ImageField(upload_to='categorias/', blank=True, null=True)
    pub_date = models.DateTimeField('fecha de registro', auto_now=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    pub_date = models.DateTimeField('fecha de registro', auto_now_add=True)

    def __str__(self):
        return self.nombre
