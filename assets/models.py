from django.db import models


class Asset(models.Model):

    EQUIPMENT_TYPES = [
        ('WEAPON', 'Weapon'),
        ('VEHICLE', 'Vehicle'),
        ('COMMUNICATION', 'Communication'),
        ('ELECTRONICS', 'Electronics'),
        ('OTHER', 'Other'),
    ]

    STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('ASSIGNED', 'Assigned'),
        ('TRANSFERRED', 'Transferred'),
        ('MAINTENANCE', 'Maintenance'),
    ]

    name = models.CharField(max_length=200)

    equipment_type = models.CharField(
        max_length=30,
        choices=EQUIPMENT_TYPES
    )

    base = models.CharField(max_length=100)

    quantity = models.PositiveIntegerField(default=0)

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='AVAILABLE'
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name