from django.shortcuts import render

def index(request):
    return render(request, 'personas/index.html')

def personas(request):
    return render(request, 'personas/personas.html')