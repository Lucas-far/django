

"""
Módulo: modelo_base.py

Objetivo:
         modelo que serve para ter seus campos herdados

Palavra chave: modelo base
"""

"abstract"  # Torna esse modelo indisponível para receber migração, pois isto é desnecessário
def models():
    """
    from django.db import models

    class Base(models.Model):
        creation = models.DateTimeField('Data de criação', auto_now_add=True)
        updated = models.DateTimeField('Última atualização', auto_now=True)
        availability = models.BooleanField('Disponível', default=True)

        class Meta:
            abstract = True
    """
