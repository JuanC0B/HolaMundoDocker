from django.shortcuts import render

def saludo(request):
    return render(request, 'saludo.html')

def home(request):
    return render(request, 'saludo.html')  # Puedes reutilizar 'saludo.html' para la página de inicio
