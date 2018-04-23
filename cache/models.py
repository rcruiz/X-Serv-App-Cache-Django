from django.db import models


class Page(models.Model):
    recurso = models.CharField(max_length=128)
    contenido = models.TextField()
    def __str__(self):
          return self.recurso
