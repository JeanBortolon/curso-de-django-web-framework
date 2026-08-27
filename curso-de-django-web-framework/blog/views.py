# Importa o tipo 'Any' do módulo 'typing' para anotações de tipo.
from typing import Any

# Importa a lista de posts do arquivo de dados local.
from blog.data import posts
# Importa exceções e classes de requisição/resposta do Django.
# Http404 é usado para retornar uma página de "não encontrado".
# HttpRequest representa uma requisição HTTP.
from django.http import Http404, HttpRequest
# Importa a função 'render' para renderizar templates HTML.
from django.shortcuts import render


# View para a página principal do blog, que lista todos os posts.
def blog(request):
    # Imprime 'blog' no console para fins de depuração.
    # Isso ajuda a confirmar que esta view específica foi chamada quando a URL correspondente é acessada.
    print('blog')

    # Cria um dicionário de contexto. O contexto é usado para passar dados do Python para o template HTML.
    context = {
        # 'text': 'Olá blog',
        # Adiciona a lista completa de posts ao contexto.
        'posts': posts
    }

    # Renderiza o template 'blog/index.html' com os dados do contexto.
    # A função `render` recebe o objeto `request`, o caminho do template e o dicionário de contexto.
    return render(
        request,
        'blog/index.html',
        context
    )


# View para exibir um único post, identificado pelo seu ID.
def post(request: HttpRequest, post_id: int):
    # Anotações de tipo: `request` é um HttpRequest, `post_id` é um inteiro.
    # Isso melhora a legibilidade e ajuda ferramentas de análise de código.
    # Inicializa a variável que armazenará o post encontrado como None.
    found_post: dict[str, Any] | None = None

    # Itera sobre a lista de dicionários de posts para encontrar aquele com o 'id' correspondente ao `post_id` recebido.
    for post in posts:
        # Verifica se o ID do post atual é igual ao post_id recebido na URL.
        if post['id'] == post_id:
            # Se encontrar, atribui o dicionário do post à variável found_post.
            found_post = post
            # Interrompe o loop, pois o post já foi encontrado.
            break

    # Se, após percorrer todos os posts, `found_post` ainda for None, significa que nenhum post com o `post_id` fornecido foi encontrado.
    if found_post is None:
        # Lança uma exceção Http404. O Django irá capturar esta exceção e renderizar uma página de erro "404 Not Found".
        raise Http404('Post não existe.')

    # Cria o contexto para passar os dados do post encontrado para o template.
    context = {
        # 'text': 'Olá blog',
        # Adiciona o dicionário do post encontrado ao contexto sob a chave 'post'.
        # Adiciona o dicionário do post encontrado ao contexto.
        'post': found_post,
        # Cria um título para a página HTML, concatenando o título do post.
        'title': found_post['title'] + ' - ',
    }

    # Renderiza o template 'blog/post.html' com os dados do post específico.
    return render(
        request,
        'blog/post.html',
        context
    )


# Uma view de exemplo para demonstrar a renderização de um template simples.
def exemplo(request):
    # Imprime 'exemplo' no console para fins de depuração.
    # Ajuda a verificar se esta view foi acessada.
    print('exemplo')

    # Cria um dicionário de contexto com dados de texto e título específicos para a página de exemplo.
    context = {
        'text': 'Olá exemplo',
        'title': 'Essa é uma página de exemplo - ',
    }

    # Renderiza o template 'blog/exemplo.html' com o contexto definido.
    return render(
        request,
        'blog/exemplo.html',
        context
    )
