from django.contrib import admin
from .models import Cliente

class ClientesAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'email',
        'phone'
    )

    list_display = (
        'name',
        'email',
        'phone'
    )

    search_fields = (
        'name',
        'phone'
    )

    list_filter = (
        'name',
        'phone'
    )

admin.site.register(Cliente, ClientesAdmin)
