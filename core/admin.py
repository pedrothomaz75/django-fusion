from django.contrib import admin

from .models import (
    Servico, Cargo, Funcionario, 
    Precos, Recursos
)



@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'modificado', 'ativo')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'modificado', 'ativo')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado', 'ativo')

@admin.register(Precos)
class PrecosAdmin(admin.ModelAdmin):
    list_display = ('preco_plano', 'plano', 'modificado')

@admin.register(Recursos)
class RecursosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modificado', 'ativo')
