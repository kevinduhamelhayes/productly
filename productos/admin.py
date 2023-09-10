from django.contrib import admin
from .models import Producto
from .models import Categoria
from .models import Cliente

class CategoriaAdmin(admin.ModelAdmin):
    exclude = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    
# Register your models here.

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Cliente)
