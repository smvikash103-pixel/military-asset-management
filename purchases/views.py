from django.shortcuts import render
from .models import Purchase


def purchases(request):

    purchases = Purchase.objects.all()

    return render(
        request,
        'purchases/purchases.html',
        {
            'purchases': purchases
        }
    )