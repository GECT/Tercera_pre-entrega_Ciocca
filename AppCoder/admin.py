from django.contrib import admin
from .models import Curso, Entregable, Estudiantes, Profesor
# Register your models here.
admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Estudiantes)
admin.site.register(Profesor)