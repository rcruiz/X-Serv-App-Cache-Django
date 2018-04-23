from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
import urllib.request


def buscar(request, rec):
    #if rec in cache # si cache es dic global
    try:
        cache = Page.objects.get(recurso=rec)
        #return HttpResponse(cache.contenido)
    except Page.DoesNotExist:
        #return HttpResponse('Nombre de la página no almacenado')
        with urllib.request.urlopen('http://' + rec) as w:
			pagina = w.read().decode('utf-8')
			#cache[rec] = pagina
            cache = Page(recurso=rec, contenido=pagina)
            cache.save()
			#resp = HttpResponse(pagina)
    return HttpResponse(cache.contenido)
