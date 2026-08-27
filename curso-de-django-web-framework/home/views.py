# Importa a função `render` do módulo `django.shortcuts`.
# A função `render` é uma forma conveniente de carregar um template, preenchê-lo com um contexto
# e retornar um objeto `HttpResponse` contendo o HTML renderizado.
from django.shortcuts import render


# Define a função de visualização chamada `home`.
# No Django, uma view é uma função Python que recebe um objeto `HttpRequest` como seu primeiro argumento
# e é responsável por retornar um objeto `HttpResponse`, que pode ser uma página HTML, um redirecionamento, um erro, etc.
def home(request):
    # Imprime 'home' no console do servidor. Isso é útil para depuração,
    # permitindo saber quando esta view específica é acessada.
    print('home')

    # Cria um dicionário de contexto.
    # O contexto é um dicionário Python que é usado para passar variáveis do código Python da view
    # para o template HTML, onde essas variáveis podem ser exibidas ou usadas para lógica de template.
    context = {
        'text': 'Olá home'  # Define uma chave 'text' com o valor 'Olá home'.
    }

    # Renderiza o template 'home/index.html' com o contexto fornecido.
    # `request`: O objeto HttpRequest que iniciou esta view.
    # `'home/index.html'`: O caminho para o template HTML que será renderizado.
    # `context`: O dicionário de contexto cujas chaves e valores estarão disponíveis no template.
    return render(
        request,
        'home/index.html',
        context,
    )
