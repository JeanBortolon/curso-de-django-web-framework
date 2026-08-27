"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
# Importa o módulo 'os' para interagir com o sistema operacional.
import os

# Importa 'get_wsgi_application' de 'django.core.wsgi' para auxiliar na implantação da aplicação.
from django.core.wsgi import get_wsgi_application

# Define a variável de ambiente 'DJANGO_SETTINGS_MODULE'. Isso informa ao Django
# qual arquivo de configurações usar. É crucial para configurar seu projeto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Obtém a aplicação WSGI. Este é o ponto de entrada principal para servidores web
# compatíveis com WSGI para servir seu projeto Django.
application = get_wsgi_application()
