from django.contrib import admin
from .models import User, Categoria, Producto

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(User)