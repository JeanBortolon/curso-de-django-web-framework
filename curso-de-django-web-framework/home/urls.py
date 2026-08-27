# Este arquivo define as configurações de URL para o aplicativo 'home' do Django.
# Ele mapeia URLs específicas para funções de visualização (views) correspondentes.

from django.urls import path # Importa a função 'path' do módulo django.urls, usada para definir padrões de URL.

from . import views # Importa o módulo 'views' do diretório atual, onde as funções que lidam com as requisições HTTP estão definidas.

app_name = 'home' # Define o namespace da aplicação. Isso ajuda a organizar as URLs e a referenciá-las de forma única em outras partes do projeto (ex: templates).

urlpatterns = [
    # Define um padrão de URL.
    # - O primeiro argumento, '', representa a raiz do aplicativo 'home' (ex: /home/).
    # - O segundo argumento, views.home, indica que a requisição para essa URL será tratada pela função 'home' definida em views.py.
    # - O argumento name='home' atribui um nome a este padrão de URL, permitindo referenciá-lo simbolicamente (ex: {% url 'home:home' %}) ao invés de usar a URL hardcoded.
    path('', views.home, name='home'),
]

