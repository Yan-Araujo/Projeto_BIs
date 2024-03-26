from django.contrib import admin
from catalogo.models import BiCard


class BiCardAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "ativo")
    list_display_links = ("id", "name")
    search_fields = ("name", "id")
    list_editable = ("ativo",)
    list_per_page = 10


admin.site.register(BiCard, BiCardAdmin)