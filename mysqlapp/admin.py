from django.contrib import admin
from .models import Questao, Participante, Opcao


class OpcaoInline(admin.TabularInline):
    model = Opcao
    extra = 1


class QuestaoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['questao_texto']}),
        ('Data', {'fields': ['data_pub'], 'classes': ['collapse']}),
    ]
    list_display = ('questao_texto', 'data_pub')
    list_filter = ['data_pub']
    search_fields = ['questao_texto']
    inlines = [OpcaoInline]


admin.site.register(Questao, QuestaoAdmin)


admin.site.register(Participante)

