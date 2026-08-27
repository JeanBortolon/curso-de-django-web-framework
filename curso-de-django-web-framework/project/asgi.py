"""
Configuração ASGI (Asynchronous Server Gateway Interface) para o projeto 'project'.

Este arquivo expõe o 'callable' ASGI como uma variável de nível de módulo chamada ``application``.
O ASGI é uma especificação para servidores web assíncronos Python e aplicações que permite
a comunicação entre eles.

Para mais informações sobre este arquivo, consulte a documentação oficial do Django:
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os # Importa o módulo 'os' para interagir com o sistema operacional

from django.core.asgi import get_asgi_application # Importa a função para obter a aplicação ASGI do Django

# Define a variável de ambiente 'DJANGO_SETTINGS_MODULE'
# Isso aponta para o arquivo de configurações do seu projeto Django,
# garantindo que o Django saiba onde encontrar suas configurações.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Obtém a aplicação ASGI padrão do Django.
# Esta é a principal entrada para servidores compatíveis com ASGI,
# como Daphne ou Uvicorn, para servir sua aplicação Django.
application = get_asgi_application()
