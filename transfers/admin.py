from django.contrib import admin
from .models import Transfer


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = (
        'asset',
        'from_base',
        'to_base',
        'quantity',
        'transfer_date',
        'created_at',
    )

    list_filter = (
        'from_base',
        'to_base',
        'transfer_date',
    )

    search_fields = (
        'asset__name',
        'from_base',
        'to_base',
    )