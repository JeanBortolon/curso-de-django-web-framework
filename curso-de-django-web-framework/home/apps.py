# Importa a classe AppConfig do módulo django.apps.
# AppConfig é a classe base para a configuração de aplicações Django.
from django.apps import AppConfig


# Define a classe de configuração para a aplicação 'home'.
# O nome da classe é geralmente o nome da aplicação com 'Config' anexado.
class HomeConfig(AppConfig):
    # Define o tipo de campo automático padrão a ser usado para chaves primárias em modelos nesta aplicação.
    # 'django.db.models.BigAutoField' é um campo de inteiro de 64 bits que automaticamente incrementa,
    # sendo uma boa prática para evitar problemas de escala com chaves primárias menores.
    default_auto_field = 'django.db.models.BigAutoField'
    # Define o nome da aplicação. Este deve corresponder ao nome do diretório da aplicação.
    name = 'home'
