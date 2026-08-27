#!/usr/bin/env python
"""Utilitário de linha de comando do Django para tarefas administrativas."""
import os
import sys


def main():
    """Executa tarefas administrativas.
    Esta função é o ponto de entrada para executar as tarefas administrativas do Django a partir da linha de comando.
    """
    # Define o módulo de configurações padrão para o Django.
    # Isso informa ao Django onde encontrar o arquivo settings.py do projeto.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        # Tenta importar a função execute_from_command_line do Django.
        # Esta função lida com a análise dos argumentos da linha de comando e a execução do comando de gerenciamento Django correspondente.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Se o Django não puder ser importado, significa que provavelmente não está instalado ou o ambiente virtual não está ativado.
        raise ImportError(
            "Não foi possível importar o Django. Tem certeza de que ele está instalado e "
            "disponível na sua variável de ambiente PYTHONPATH? Você se "
            "esqueceu de ativar um ambiente virtual?"
        ) from exc
    # Executa a tarefa da linha de comando usando os argumentos fornecidos.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Isso garante que main() seja chamado apenas quando o script for executado diretamente,
    # não quando for importado como um módulo.
    main()
