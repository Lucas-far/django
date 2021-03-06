

"""
Módulo: testes.py
Objetivo: exemplificar uma maneira de teste comum para projetos Django
Palavra chave: tutorial teste
"""

def fonte():
    """
    Curso  # Programação Web com Python e Django framework: Essencial
    Seção  # Seção 6:Testando seu projeto
    Aula   # 59. Entendendo e configurando os testes
    Minuto # 08:27
    """

"-------------------------------------------- COMANDO PARA EXECUTAR TESTES --------------------------------------------"

# pythton manage.py test

"------------------------------------------------ EXEMPLO: TESTE COMUM ------------------------------------------------"


def teste_regular():
    """
    from django.test import TestCase

    def remover_vogais(string):
        container = []

        vowels = ['a', 'e', 'i', 'o', 'u',
                  'à', 'á', 'â', 'ã',
                  'é',
                  'í',
                  'ó', 'ô', 'õ', 'ò'
                  'ú',
                  ]

        for lt in string:
            container.append(lt)
        for lt in vowels:
            while lt in container:
                container.pop(container.index(lt))
        container = ''.join(container)
        return container

    class FirstTestCase(TestCase):
        def setUp(self):
            self.texto = 'Lucas Farias Santos de Sousa'

        def test_remover_vogais(self):
            frase = remover_vogais(self.texto)
            self.assertTrue(frase == 'Lcs Frs Snts d Ss')
    """

def terminal():
    """
    pip install django==2.2.17
    pip install django-bootstrap4
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    INSTALLED_APPS = ['pa', 'bootstrap4']
    TEMPLATES = 'DIRS': ['templates']
    """

def models():
    """
    from django.db import models

    class Modelo(models.Model):
        texto = models.CharField('Texto', max_length=500)

        class Meta:
            verbose_name = 'Texto'
            verbose_name_plural = 'Textos'

        def __str__(self):
            return self.texto
    """

def admin():
    """
    from django.contrib import admin
    from .models import *

    @admin.register(Modelo)
    class ModeloAdmin(admin.ModelAdmin):
        list_display = ('texto',)
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    """


"raiz/pa/tests.py"               # módulo padrão para testes no Django (não recomendável)
"raiz/new/python package/tests"  # ação recomendável

# Módulos a serem criados dentro do pacote [ tests ]

"tests/new/python file/test_models"
"tests/new/python file/test_forms"
"tests/new/python file/test_views"

def terminal3():
    """
    pip install model_mommy
    pip install coverage
    pip freeze > requirements.txt
    """

def pa_tests():
    """
    raiz/new/python package/tests -----> tests/new/python file/test_models
    """

"class ModeloTestCase"             # nome do modelo no módulo [ models.py ] + TestCase
"self.var = mommy.make('Modelo')"  # uso da biblioteca model_mommy para auxiliar em testes no módulo [ models.py ]
def test_models():
    """
    from django.test import TestCase
    from model_mommy import mommy

    class ModeloTestCase(TestCase):
        def setUp(self):
            self.var = mommy.make('Modelo')

        def test_str(self):
            self.assertEquals(str(self.var), self.var.texto)
    """

"raiz/new/file/.coveragerc"  # criar módulo para filtrar módulos a serem testados
"OBS"                        # após todos os testes passarem, é uma boa ideia adicionar a esse módulo: [ htmlcov/* ]
def raiz():
    """
    [run]
    source = .

    omit =
        */__init__.py
        */settings.py
        */manage.py
        */wsgi.py
        */apps.py
        */urls.py
        */admin.py
        */migrations/*
        */tests/*
    """

# Após criar o módulo acima, executa-se o teste, que busca, no projeto, um diretório chamado: [ tests ]
def terminal4():
    """ coverage run manage.py test """

# Comandos posteriores ao teste
def terminal5():
    """
    1. coverage report       || exibir relatório do progresso dos testes, em módulos filtrados, via terminal
    2. coverage html         || criar um diretório do progresso dos testes, para vê-los em um servidor local
    3. python -m http.server || acessar o servidor local de testes
    4. rm -rf htmlcov        || deletar o diretório de testes (normalmente usado após ter progresso nos testes)
    """
    # Lógica: a cada progresso em %, deleta-se o diretório de testes, e recria-se este (2 ao 4)
