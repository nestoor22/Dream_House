from django.shortcuts import render


def index(request):
    return render(request, 'graphsPage.html', {'onclick': 'return true'})