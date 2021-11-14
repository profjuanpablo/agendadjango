from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','telefone','email','data_criacao')
    list_display_links = ('id','nome','sobrenome')

admin.site.register(Categoria)
admin.site.register(Contato,ContatoAdmin)