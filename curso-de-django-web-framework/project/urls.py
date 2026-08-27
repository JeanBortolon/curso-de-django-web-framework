"""
Configuração de URL para o projeto principal.

A lista `urlpatterns` encaminha URLs para as views. Para mais informações, por favor, veja:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Exemplos:
Function views (Views baseadas em função)
    1. Importe: from my_app import views
    2. Adicione uma URL a urlpatterns: path('', views.home, name='home')
Class-based views (Views baseadas em classe)
    1. Importe: from other_app.views import Home
    2. Adicione uma URL a urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf (Incluindo outro arquivo de configuração de URL)
    1. Importe a função include(): from django.urls import include, path
    2. Adicione uma URL a urlpatterns: path('blog/', include('blog.urls'))
"""
# Importa módulos necessários do Django
from django.contrib import admin  # Importa o módulo de administração do Django
from django.urls import include, path  # Importa as funções include e path para roteamento de URLs

# urlpatterns define o roteamento de URLs do projeto
urlpatterns = [
    # Mapeia a URL raiz ('') para as URLs da aplicação 'home'
    # 'include' é usado para incorporar arquivos urls.py de outras aplicações
    path('', include('home.urls')),
    # Mapeia URLs que começam com 'blog/' para as URLs da aplicação 'blog'
    path('blog/', include('blog.urls')),
    # Mapeia URLs que começam com 'admin/' para as URLs do painel administrativo do Django
    path('admin/', admin.site.urls),
]

