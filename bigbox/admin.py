from django.contrib import admin
from .models import Box, Activity, Category, Reason

# Register your models here.

# 3) Crear el siguiente archivo bigbox/admin.py y crear la vista del admin para los 4
# modelos(Box, Activity, Category y Reason), Que me permita realizar un CRUD (Crear,
# Leer, Actualizar y Borrar) a cada uno de los modelos (Box, Activity, Category y Reason).

# admin.site.register(Box)

class BoxAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Box, BoxAdmin)
admin.site.register(Activity)
admin.site.register(Category)
admin.site.register(Reason)
