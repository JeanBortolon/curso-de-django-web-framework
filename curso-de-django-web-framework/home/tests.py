# Este arquivo é dedicado aos testes unitários para o aplicativo 'home' do Django.
# Testes são cruciais para garantir que as funcionalidades do seu aplicativo funcionem como esperado.

# Importa a classe 'TestCase' do módulo `django.test`.
# `TestCase` é a classe base para a criação de testes no Django,
# fornecendo métodos úteis para simular requisições HTTP, interagir com o banco de dados de teste, etc.
from django.test import TestCase
from django.urls import reverse # Importa a função reverse para resolver URLs a partir de seus nomes.

# Create your tests here.
# A partir daqui, você pode definir suas classes de teste.
# Cada classe de teste deve herdar de TestCase.
# Um exemplo básico de como você poderia começar a escrever testes:

# Define uma classe de teste para as views do aplicativo 'home'.
class HomeViewTest(TestCase):
    def test_home_page_status_code(self):
        # Testa se a página inicial (mapeada para 'home:home') está acessível e retorna um código de status 200 (OK).
        url = reverse('home:home') # Usa reverse() para obter a URL da view 'home' no namespace 'home'.
        response = self.client.get(url) # Simula uma requisição GET para essa URL.
        self.assertEqual(response.status_code, 200) # Verifica se o código de status da resposta HTTP é 200.

    def test_home_page_uses_correct_template(self):
        # Testa se a página inicial está usando o template HTML correto para sua renderização.
        url = reverse('home:home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home/index.html') # Verifica se o template 'home/index.html' foi usado.

# Lembre-se de rodar seus testes usando: python manage.py test home
