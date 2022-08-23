import http
from cgitb import reset
from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Henrique Cesar'

    })

def contato(request):
    return render(request, 'me_apague/tempo.html')

def sobre(request):
    return HttpResponse('sobre')
