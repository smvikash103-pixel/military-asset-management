from django.contrib import admin
from .models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        'asset',
        'quantity',
        'base',
        'supplier',
        'purchase_date',
        'unit_cost',
        'total_cost',
    )

    list_filter = (
        'base',
        'purchase_date',
    )

    search_fields = (
        'asset__name',
        'supplier',
    )