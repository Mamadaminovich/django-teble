from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def home(request):
    context = {
        "qator": [
            ["Baseball", 29, 0, 29],
            ["Baseball", 29, 0, 29],
            ["Baseball", 29, 0, 29],
            ["Baseball", 29, 0, 29],
        ]
    }
    return render(request, 'index.html', context)

def message(request):
    return HttpResponse('<h1>Bu message qismi</h1>')