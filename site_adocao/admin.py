from django.contrib import admin

from site_adocao.models import Apoio, Cachorro, Gato, Outro


class Apoios(admin.ModelAdmin):
    list_display = ('id','nome','contato')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Apoio, Apoios)

class Cachorros(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Cachorro, Cachorros)

class Gatos(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Gato, Gatos)

class Outros(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Outro, Outros)



