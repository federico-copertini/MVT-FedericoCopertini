from django.contrib import admin

# Register your models here.
from .models import Familiar

class FamiliarAdmin(admin.ModelAdmin):
    list_display = ("nombre","apellido","edad","rol","fecha_de_nacimiento")

admin.site.register(Familiar, FamiliarAdmin)