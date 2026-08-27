# Importa a classe TestCase para criar testes unitários no Django.
# Importa a classe TestCase para criar testes unitários no Django.
from django.test import TestCase
# Importa a função reverse para resolver URLs a partir de seus nomes,
# tornando os testes mais robustos e fáceis de manter.
from django.urls import reverse

# Este arquivo, tests.py, é onde você escreve os testes para sua aplicação 'blog'.
# Testes são essenciais para garantir que seu código funcione como esperado e
# para prevenir regressões (introduzir novos bugs em funcionalidades existentes) ao longo do tempo.

# Crie seus testes aqui.

# Abaixo, um exemplo de como você poderia começar a escrever testes para as views do seu app 'blog'.
# As classes de teste herdam de django.test.TestCase e os métodos de teste começam com 'test_'.

class BlogViewsTest(TestCase):
    def test_blog_view_status_code_is_200_ok(self):
        # Testa se a página principal do blog (listagem de posts) está acessível.
        # A função reverse() busca a URL correspondente ao nome 'home' dentro do namespace 'blog'.
        url = reverse('blog:home')
        # O self.client simula um navegador fazendo uma requisição GET para a URL.
        response = self.client.get(url)
        # self.assertEqual() verifica se o status da resposta HTTP é 200 (OK), indicando sucesso.
        self.assertEqual(response.status_code, 200)

    def test_blog_view_uses_correct_template(self):
        # Testa se a view 'blog' (que exibe a lista de posts) renderiza o template HTML correto.
        response = self.client.get(reverse('blog:home'))
        # self.assertTemplateUsed() verifica se o template especificado foi usado para renderizar a resposta.
        self.assertTemplateUsed(response, 'blog/index.html')

    # def test_post_view_returns_404_if_post_does_not_exist(self):
    #     # Testa se a view 'post' retorna um erro 404 para um ID de post que não existe.
    #     # Usamos um ID muito alto (9999) que provavelmente não existirá no nosso conjunto de dados de teste.
    #     url = reverse('blog:post', kwargs={'post_id': 9999})
    #     response = self.client.get(url)
    #     # Verifica se o status da resposta é 404 (Not Found), conforme esperado para um post inexistente.
    #     self.assertEqual(response.status_code, 404)

# Para rodar os testes deste aplicativo 'blog', use o comando no terminal na raiz do seu projeto Django:
# python manage.py test blog
