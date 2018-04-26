from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Page
import urllib.request

def hola(request):
    return HttpResponse('Hola. Ésta es la Caché de Contenidos')

def buscar(request, rec):
    # if rec in cache: # si cache es dic global
    try:
        cache = Page.objects.get(recurso=rec)
    except Page.DoesNotExist:
        try:
            with urllib.request.urlopen('http://' + rec) as w:
                pagina = w.read().decode('utf-8')
                # cache[rec] = pagina
                cache = Page(recurso=rec, contenido=pagina)
                cache.save()
        except urllib.error.URLError:
            # return HttpResponse(e.reason)
            return HttpResponseNotFound('Error 404: Recurso no disponible.')
    return HttpResponse(cache.contenido)
