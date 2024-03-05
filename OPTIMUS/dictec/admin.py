
from django.contrib import admin

from .models import Curso, Ciclo, Calificacion, Docente, Carrera, Grado

# modelos

class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'activo', 'creacion')
admin.site.register(Curso, CursoAdmin)

class CicloAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'activo', 'creacion')
admin.site.register(Ciclo, CicloAdmin)

class CarreraAdmin(admin.ModelAdmin):
    readonly_fields = ('nombre', 'activo')
admin.site.register(Carrera, CarreraAdmin)

class GradoAdmin(admin.ModelAdmin):
    readonly_fields = ('llama', 'activo')
admin.site.register(Grado, GradoAdmin)

class CalificacionAdmin(admin.ModelAdmin):
    readonly_fields = ( 'grado', 'curso', 'docente')
    list_display = ( 'grado', 'curso', 'docente')
admin.site.register(Calificacion, CalificacionAdmin)

class DocenteAdmin(admin.ModelAdmin):
    readonly_fields = ('cargo',)
admin.site.register(Docente, DocenteAdmin)