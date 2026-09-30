from django.shortcuts import render

def assignments(request):
    return render(request, 'assignments/assignments.html')