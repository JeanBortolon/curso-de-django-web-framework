from django.apps import AppConfig


# Define a classe de configuração para o aplicativo 'blog'.
# Cada aplicativo Django deve ter uma classe AppConfig.
class BlogConfig(AppConfig):
    # Define o tipo de campo padrão para chaves primárias automáticas.
    # 'BigAutoField' é recomendado para a maioria dos projetos, pois fornece um intervalo maior
    # de valores para IDs, evitando problemas de estouro em bancos de dados grandes.
    default_auto_field = 'django.db.models.BigAutoField'
    # Define o nome do aplicativo. Este nome é usado pelo Django para identificar o aplicativo
    # em várias partes do framework, como em 'INSTALLED_APPS' no settings.py.
    name = 'blog'
