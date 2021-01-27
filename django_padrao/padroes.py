

"""
Módulo: padroes.py
Objetivo: inserir as configurações iniciais para um projeto Django
Palavra chave: padrao inicial
"""

def terminal():
    """
    pip install django==2.2.17 django-bootstrap4
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    python manage.py migrate
    python manage.py createsuperuser
    """

def settings():
    """
    INSTALLED_APPS = ['pa', 'bootstrap4']
    TEMPLATES = 'DIRS': ['templates']
    """

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """

def pa_urls():
    """
    from django.urls import path
    from .views import *

    urlpatterns = [
        # path('', index, name='index'),
        # path('', IndexTemplateView.as_view(), name='index'),
    ]
    """

def templates():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="#" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página</title>
    </head>
    <body>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """
