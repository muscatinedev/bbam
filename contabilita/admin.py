from django.contrib import admin
from .models import Movimento, Conto, Operazione


class ContoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'ambito']

    def get_ordering(self, request):
        return ['id']  # sort case insensitive


admin.site.register(Conto, ContoAdmin)


class OperazioneAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'dare', 'avere']

    def get_ordering(self, request):
        return ['id']  # sort case insensitive


admin.site.register(Operazione, OperazioneAdmin)


class MovimentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'dataMovimento', 'operazione', 'importo', 'natura', ]

    def get_ordering(self, request):
        return ['-dataMovimento']  # sort case insensitive


admin.site.register(Movimento, MovimentoAdmin)
