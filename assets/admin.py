from django.contrib import admin
from .models import Asset


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'equipment_type',
        'base',
        'quantity',
        'status',
        'created_at',
    )

    list_filter = (
        'equipment_type',
        'base',
        'status',
    )

    search_fields = (
        'name',
        'base',
    )