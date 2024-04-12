from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from apps.usuarios.models import UsuariosModel

class CustomUserAdmin(UserAdmin):
    
    list_display = (
        'id',
        'email',
        'identificacion',
        'is_superuser',
        'cliente',
        'fecha_creacion',
    )
    ordering = ('-id',)

    fieldsets = (
        ('Información General', {'fields': ('username', 'email', 'password', 'date_joined', 'is_superuser', 'is_staff', 'user_permissions',)}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'identificacion', 'prefijo_telefono', 'telefono', 'genero_usuario',)}),
        ('Datos adicionales', {'fields': ('activo', 'estado_sesion', 'cliente')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ['email', 'identificacion', 'telefono',]
    filter_horizontal = ['user_permissions',]

admin.site.register(UsuariosModel, CustomUserAdmin)