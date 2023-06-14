from django.contrib import admin
from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('display_id', 'display_username', 'display_nombre', 'display_apellido', 'display_email', 'display_telefono')
    search_fields = ('id', 'username')

    def display_id(self, obj):
        return obj.id
    display_id.short_description = 'ID'

    def display_username(self, obj):
        return obj.username
    display_username.short_description = 'Username'

    def display_nombre(self, obj):
        return obj.nombre
    display_nombre.short_description = 'Nombre'

    def display_apellido(self, obj):
        return obj.apellido
    display_apellido.short_description = 'Apellido'

    def display_email(self, obj):
        return obj.email
    display_email.short_description = 'Email'

    def display_telefono(self, obj):
        return obj.telefono
    display_telefono.short_description = 'Teléfono'

    # Registrar el modelo Usuario con el UsuarioAdmin personalizado
admin.site.register(Usuario, UsuarioAdmin)
