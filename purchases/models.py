from django.db import models
from assets.models import Asset


class Purchase(models.Model):
    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        related_name='purchases'
    )
    quantity = models.PositiveIntegerField()
    base = models.CharField(max_length=100)
    supplier = models.CharField(max_length=200)
    purchase_date = models.DateField()
    unit_cost = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def total_cost(self):
        return self.quantity * self.unit_cost

    def __str__(self):
        return f"{self.asset.name} - {self.quantity}"