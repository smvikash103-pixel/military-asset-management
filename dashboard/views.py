from django.shortcuts import render
from assets.models import Asset


def dashboard(request):

    # Get total quantity of all assets
    total_assets = sum(
        asset.quantity
        for asset in Asset.objects.all()
    )

    # Count assigned assets
    assigned_assets = sum(
        asset.quantity
        for asset in Asset.objects.filter(status='ASSIGNED')
    )

    # Current assets in the system
    opening_balance = total_assets

    # No purchases/transfers are connected yet
    closing_balance = total_assets

    # Movement will be calculated when we add
    # Purchases and Transfers modules
    net_movement = 0

    total_transfers = 0

    context = {
        'opening_balance': opening_balance,
        'closing_balance': closing_balance,
        'net_movement': net_movement,
        'assigned_assets': assigned_assets,
        'total_transfers': total_transfers,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )