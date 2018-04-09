# X-Serv-App-Cache-Django
Ejercicio de asignaturas de aplicaciones web. Servicios que interoperan. Cache de contenidos versión Django.

## Enunciado

Vamos a construir una aplicación web que no sólo recibe peticiones de un cliente, sino que también hace peticiones a otros servicios web. El ejercicio consiste en construir una aplicación que, dada una URL (sin `http://`) como nombre de recurso, devuelve el contenido de la página correspondiente a esa URL. Esto es, si se le pide http://localhost:1234/gsyc.es/ devuelve el contenido de la página http://gsyc.es/. Además, lo guarda en un diccionario, de forma que si se le vuelve a pedir, lo devuelve directamente de ese diccionario.

Construir la aplicación sobre Django. Puede usarse como base [Django cms](https://github.com/CursosWeb/X-Serv-15.5-Django-CMS), y si se quiere, el módulo estándar de Python [urllib](https://docs.python.org/3/library/urllib.html).
