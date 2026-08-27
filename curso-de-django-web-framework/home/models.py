# Importa o módulo models do Django, que contém as classes e funções necessárias para definir modelos de banco de dados.
from django.db import models

# Este arquivo é o local onde você define seus modelos de dados para o aplicativo 'home'.
# Este é o local onde você define seus modelos de dados.
# Cada modelo é uma classe que herda de `models.Model`.
# Ele representa uma tabela no banco de dados e seus atributos (campos)
# representam as colunas dessa tabela.
#
# Exemplo:
# class MyModel(models.Model): # Defina sua classe de modelo, herdando de models.Model.
#     name = models.CharField(max_length=100) # Um campo de texto curto, com um comprimento máximo.
#     description = models.TextField() # Um campo de texto longo.
#     created_at = models.DateTimeField(auto_now_add=True) # Um campo de data e hora que é preenchido automaticamente na criação.
