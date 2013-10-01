from django.contrib import admin
from principal.models import *


class VinculacionAdmin(admin.ModelAdmin):
    list_display = ["vinculacion"]
    search_fields = ["vinculacion"]

class PropositoAdmin(admin.ModelAdmin):
    list_display = [ "proposito", "vinculacion"]
    search_fields = [ "proposito"]
    


      
class MarcacionAdmin(admin.ModelAdmin):
    list_display = ["proposito", "cumplimiento"]
    search_fields = ["proposito"]
    


admin.site.register(Vinculacion, VinculacionAdmin)
admin.site.register(Proposito, PropositoAdmin)
admin.site.register(Marcacion, MarcacionAdmin)
admin.site.register(Tipo_marcacion)

