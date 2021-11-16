from django.contrib import admin

# Register your models here.
from .models import Pessoa


class ListarPessoa(admin.ModelAdmin):
    list_display = ('id','nome', 'email')
    list_display_links = ('id', 'nome')


admin.site.register(Pessoa, ListarPessoa)
