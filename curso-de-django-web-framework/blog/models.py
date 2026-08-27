# Importa o módulo models do Django, que contém as classes e funções
# necessárias para definir os "modelos" de banco de dados.
from django.db import models
from django.contrib.auth.models import User # Importa o modelo User padrão do Django para criar uma relação.

# Este arquivo (models.py) é onde você define os modelos de dados para a sua aplicação 'blog'.
# Um modelo é a fonte única e definitiva de informações sobre seus dados.
# Ele contém os campos e comportamentos essenciais dos dados que você está armazenando.
# Cada modelo corresponde a uma única tabela no banco de dados.

# Crie seus modelos aqui.

# Exemplo de como você poderia definir um modelo 'Post':
class Post(models.Model):
    # Campo para o título do post. CharField é para strings curtas a médias.
    # max_length é obrigatório e define o tamanho máximo da string.
    title = models.CharField(max_length=255)
    # Campo para um "slug" (parte amigável da URL). Deve ser único para cada post.
    # unique=True garante que não haverá slugs duplicados no banco de dados.
    slug = models.SlugField(unique=True)
    # Chave estrangeira para o modelo User do Django. Indica que um post pertence a um usuário.
    # on_delete=models.CASCADE significa que se o usuário for deletado, todos os seus posts também serão.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Campo para o corpo (conteúdo principal) do post. TextField é para strings longas.
    body = models.TextField()
    # Data e hora de criação do post. auto_now_add=True define a data/hora automaticamente na criação.
    created_at = models.DateTimeField(auto_now_add=True)
    # Data e hora da última atualização do post. auto_now=True atualiza a data/hora a cada salvamento.
    updated_at = models.DateTimeField(auto_now=True)

    # Método mágico que define a representação em string de um objeto Post.
    # Útil para o painel administrativo e depuração.
    def __str__(self):
        return self.title

# Depois de definir ou alterar seus modelos, você precisa criar e aplicar as migrações
# para que o Django atualize o esquema do banco de dados:
# 1. python manage.py makemigrations blog
# 2. python manage.py migrate
