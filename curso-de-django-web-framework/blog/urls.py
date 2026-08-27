# Importa as views (funções que lidam com as requisições HTTP) do aplicativo 'blog'.
from blog import views
# Importa a função 'path' do módulo django.urls, que é usada para definir padrões de URL.
from django.urls import path

# Define o namespace da aplicação. Isso ajuda a organizar as URLs e a referenciá-las
# de forma única em outras partes do projeto (ex: templates), evitando conflitos
# com URLs de outros aplicativos que possam ter nomes semelhantes.
app_name = 'blog'

# A lista `urlpatterns` define o roteamento de URLs para o aplicativo 'blog'.
# Cada item na lista é uma função `path()` que mapeia uma URL para uma view.
# O Django processa esses padrões em ordem, do primeiro ao último.
urlpatterns = [
    # Mapeia a URL raiz do aplicativo 'blog' (ex: /blog/ se incluído no projeto principal) para a view `views.blog`.
    # O nome 'home' é usado para referenciar esta URL simbolicamente em templates ou outras views (ex: {% url 'blog:home' %}).
    path('', views.blog, name='home'),
    # Mapeia URLs no formato '<inteiro>/' (ex: /blog/1/, /blog/5/) para a view `views.post`.
    # `<int:post_id>` é um conversor de caminho que captura um número inteiro da URL e o passa como argumento nomeado `post_id` para a função `views.post`.
    # O nome 'post' é usado para referenciar esta URL (ex: {% url 'blog:post' post_id=1 %}).
    path('<int:post_id>/', views.post, name='post'),
    # Mapeia a URL 'exemplo/' para a view `views.exemplo`.
    # O nome 'exemplo' é usado para referenciar esta URL (ex: {% url 'blog:exemplo' %}).
    path('exemplo/', views.exemplo, name='exemplo'),
]
