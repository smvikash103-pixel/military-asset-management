from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Dashboard
    path('', include('dashboard.urls')),

    # Products
    path('products/', include('products.urls')),

    # Purchases
    path('purchases/', include('purchases.urls')),

    # Transfers
    path('transfers/', include('transfers.urls')),

    # Assignments
    path('assignments/', include('assignments.urls')),

    # Expenditures
    path('expenditures/', include('expenditures.urls')),
]