from django.contrib import admin
from gu.models import Expediente,Audiencia, Participante,Grupo


admin.site.site_header = 'Administracion de Espacio Dialogo'

class ExpedienteAdmin(admin.ModelAdmin):
    list_display = ('numero','nombre','grup',)

class AudienciaAdmin(admin.ModelAdmin):
    list_display = ('fecha','exp','grup',)

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('dni','mail',)

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('id','tamaño',)

admin.site.register(Expediente, ExpedienteAdmin)
admin.site.register(Audiencia, AudienciaAdmin)
admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Grupo, GrupoAdmin)
