from django.contrib import admin
from .models import Page

# Configuración en el panel de administración
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at')
    ordering = ('created_at',)

# Registrar los campos de la base de datos
admin.site.register(Page, PageAdmin)


# Configuración del panel de administración
title = "Panel de Gestión"
subtitle = "Proyecto Web con Django y Python"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle