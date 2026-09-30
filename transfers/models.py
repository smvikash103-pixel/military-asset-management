from django.db import models
from assets.models import Asset


class Transfer(models.Model):

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE
    )

    from_base = models.CharField(max_length=100)

    to_base = models.CharField(max_length=100)

    quantity = models.PositiveIntegerField()

    transfer_date = models.DateField()

    remarks = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset.name} - {self.from_base} to {self.to_base}"