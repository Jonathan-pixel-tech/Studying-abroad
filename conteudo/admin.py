from django.contrib import admin
from .models import Pais, Universidade, CollegeList, ListaNews

class PaisAdmin(admin.ModelAdmin):
    list_display = ('nome_pais', 'lingua_oficial', 'continente')
    list_display_links = ('nome_pais',)


class UniversidadeAdmin(admin.ModelAdmin):
    list_display = ('nome_universidade',)
    list_display_links = ('nome_universidade',)

admin.site.register(Universidade, UniversidadeAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(CollegeList)
admin.site.register(ListaNews)

