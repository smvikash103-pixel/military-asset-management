from django.urls import path
from . import views

urlpatterns = [
    path('', views.expenditures, name='expenditures'),
]