

"""
Módulo: migrations.py

Objetivo: deletar migrações de forma segura, evitando gerar bugs no projeto, caso haja remoção manual
"""

# Comandos
def parte1():
    """
    1 - find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    2 - find . -path "*/migrations/*.pyc"  -delete
    3 - corrigir possíveis erros
    4 - python manage.py makemigrations
    5 - python manage.py migrate
    6 - python manage.py runserver
    """
