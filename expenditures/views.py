from django.shortcuts import render

def expenditures(request):
    return render(request, 'expenditures/expenditures.html')