from django.contrib import admin
from .models import Producto
from .models import Categoria
from .models import Cliente


# Register your models here.

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Cliente)
