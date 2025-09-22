from .models import Categoria

def categorias_globales(request):
    return {'categorias_menu': Categoria.objects.all().order_by('nombre')}