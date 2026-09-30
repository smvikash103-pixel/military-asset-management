from django.shortcuts import render
from .models import Transfer


def transfers(request):
    transfers = Transfer.objects.all()

    return render(
        request,
        'transfers/transfers.html',
        {
            'transfers': transfers
        }
    )