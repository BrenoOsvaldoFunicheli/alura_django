from django.contrib import admin

from .models import Receita

# Register your models here.


class ListandoReceita(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'publicado')
    # fields that provide direct access
    list_display_links = ('id', 'nome_receita',)
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)  # filters on the side
    list_editable = ('publicado',)
    
    list_per_page = 2

    


admin.site.register(Receita, ListandoReceita)
