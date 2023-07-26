from django.db import models
from stdimage.models import StdImageField

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificados = models.DateField('Atualização', auto_now=True)
    ativos = models.BooleanField('Ativo ?', default=True)

    class Meta:
        abstract = True

class Ser
