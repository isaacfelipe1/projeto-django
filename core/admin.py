from django.contrib import admin
from .models import Produto, Cliente
# Register your models here.
#este cara adiciona os nossos modelos para que reflita na adminitração do django
#configura a nossa aplicação
class ProdutoAdmin(admin.ModelAdmin):
    list_display=('nome','preco','estoque')
class  ClienteAdmin(admin.ModelAdmin):
    list_display=('nome', 'sobrenome','email')
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente,ClienteAdmin)