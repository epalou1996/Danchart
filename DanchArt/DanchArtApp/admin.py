from django.contrib import admin
from DanchArtApp import models
# Register your models here.

class AdminFoto(admin.ModelAdmin):
    search_fields= ('nombre', 'fecha', 'tipo')
    list_display=('nombre','fecha', 'tipo')
    list_filter=('nombre','fecha','tipo',)
    date_hierarchy = 'fecha'
      
class AdminCliente(admin.ModelAdmin):
    search_fields= ('nombre', 'apellido', 'pais', 'ciudad')
    list_display=('nombre','apellido', 'pais')
    list_filter=('nombre','apellido', 'pais', )

    

class AdminBase(admin.ModelAdmin):
    search_fields= ('nombre',)
    list_display=('nombre','base')


    

class AdminCuadro(admin.ModelAdmin):
    search_fields= ('cliente','tipo',)
    list_display=('cliente','cuadro', 'tipo')
    
   

class AdminPedido(admin.ModelAdmin):
    search_fields= ('cliente',)
    list_display=('cliente','fecha')
    list_filter=('cliente','fecha',)
    date_hierarchy = 'fecha'
    

admin.site.register(models.Foto,AdminFoto)
admin.site.register(models.Cliente,AdminCliente)
admin.site.register(models.Base,AdminBase)
admin.site.register(models.Cuadro,AdminCuadro)
admin.site.register(models.Pedido,AdminPedido)