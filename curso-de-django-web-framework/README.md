# Curso de Django

Este repositório contém um projeto Django simples, estruturado para demonstrar conceitos fundamentais do framework. A seguir, uma explicação dos arquivos e pastas principais:

## Estrutura do Projeto

### Arquivos na Raiz

*   `db.sqlite3`: Este é o banco de dados padrão do projeto. Django utiliza SQLite por padrão, que é um banco de dados baseado em arquivo, ideal para desenvolvimento local e pequenos projetos.
*   `manage.py`: Um utilitário de linha de comando para interagir com o projeto Django. Com ele, você pode executar comandos como `runserver` (para iniciar o servidor de desenvolvimento), `makemigrations` (para criar migrações de banco de dados) e `migrate` (para aplicar as migrações).
*   `requirements.txt`: Lista todas as bibliotecas Python (e suas versões) necessárias para o projeto. É usado para recriar o ambiente de desenvolvimento em outras máquinas usando `pip install -r requirements.txt`.

### Diretórios Principais

*   `base/`: Esta pasta é usada para arquivos globais do projeto que não pertencem a uma aplicação específica.
    *   `global/`: Contém templates HTML que são comuns a várias partes do site, como:
        *   `base.html`: O template base que define a estrutura comum de todas as páginas (cabeçalho, rodapé, etc.).
        *   `partials/`: Contém pequenos pedaços de templates (partials) que podem ser incluídos em outros templates, como `head.html` (para tags dentro do `<head>`) e `menu.html` (para a barra de navegação).
        *   `postblock.html`: Provavelmente um template parcial para exibir um bloco de postagens de blog.
    *   `static/`: Contém arquivos estáticos globais, como folhas de estilo CSS, JavaScript e imagens.
        *   `global/css/style.css`: A folha de estilo CSS principal para o design global do site.

*   `blog/`: Esta é uma aplicação Django. Em Django, projetos são divididos em "apps", que são módulos que lidam com uma funcionalidade específica (neste caso, um blog).
    *   `__init__.py`: Indica que `blog` é um pacote Python.
    *   `admin.py`: Registra os modelos do `blog` no painel de administração do Django, permitindo gerenciar o conteúdo do blog através de uma interface web.
    *   `apps.py`: Define a configuração para a aplicação `blog`.
    *   `data.py`: Pode conter dados de exemplo ou funções para popular o banco de dados com dados iniciais para o blog.
    *   `models.py`: Define as estruturas de dados (modelos) do blog, como `Post`, `Author`, `Category`, etc. Estes modelos representam as tabelas no banco de dados.
    *   `README.md`: Documentação específica para a aplicação `blog`.
    *   `tests.py`: Contém testes automatizados para a aplicação `blog` (por exemplo, testar se os modelos estão funcionando corretamente ou se as views retornam o esperado).
    *   `urls.py`: Define as rotas (URLs) específicas para a aplicação `blog`, mapeando URLs para as funções de visualização (views).
    *   `views.py`: Contém as funções que lidam com a lógica de requisições HTTP e retornam as respostas (geralmente renderizando templates HTML).
    *   `__pycache__/`: Pasta gerada automaticamente pelo Python para armazenar arquivos compilados (`.pyc`), otimizando o carregamento do módulo.
    *   `migrations/`: Contém arquivos que descrevem as alterações no esquema do banco de dados (criadas com `manage.py makemigrations`).
    *   `templates/blog/`: Contém os templates HTML específicos da aplicação `blog`, como `index.html` (para a listagem de posts) e `post.html` (para a visualização de um único post). `exemplo.html` é provavelmente um template de exemplo ou teste.

*   `home/`: Outra aplicação Django, similar ao `blog/`, mas para a página inicial ou outras funcionalidades não relacionadas ao blog.
    *   A estrutura e o propósito dos arquivos (`__init__.py`, `admin.py`, `apps.py`, `models.py`, `tests.py`, `urls.py`, `views.py`, `__pycache__/`, `migrations/`, `templates/home/`) são análogos aos da aplicação `blog/`, mas focados na funcionalidade "home".

*   `project/`: Esta é a pasta de configuração principal do projeto Django.
    *   `__init__.py`: Indica que `project` é um pacote Python.
    *   `asgi.py`: Um ponto de entrada para servidores compatíveis com ASGI (Asynchronous Server Gateway Interface), usado para aplicações assíncronas.
    *   `settings.py`: O arquivo de configuração central do projeto. Contém definições como `INSTALLED_APPS` (quais apps estão ativas), `DATABASES` (configuração do banco de dados), `STATIC_URL` (URL para arquivos estáticos), etc.
    *   `urls.py`: O arquivo de URLs raiz do projeto. Ele inclui as URLs de todas as aplicações (como `blog/urls.py` e `home/urls.py`).
    *   `wsgi.py`: Um ponto de entrada para servidores compatíveis com WSGI (Web Server Gateway Interface), usado para aplicações síncronas.

*   `venv/`: Esta pasta representa o ambiente virtual Python.
    *   `Scripts/`: Contém os executáveis Python e `pip` específicos para este ambiente virtual.
    *   `Lib/site-packages/`: Armazena as bibliotecas Python instaladas via `pip install -r requirements.txt`, isolando-as das bibliotecas do sistema.

## Conceitos Estudados (Inferidos pela Estrutura)

Com base na estrutura de arquivos, os seguintes conceitos de Django foram provavelmente estudados:

1.  **Estrutura de Projetos e Aplicações:** Como organizar um projeto Django em apps reutilizáveis.
2.  **Modelos (Models):** Como definir a estrutura do banco de dados usando classes Python em `models.py`.
3.  **Views (Views):** Como escrever funções em `views.py` que recebem requisições web e retornam respostas.
4.  **Templates (Templates):** Como criar arquivos HTML em `templates/` para renderizar o conteúdo dinamicamente, incluindo o uso de templates base (`base.html`) e parciais (`partials/`).
5.  **URLs (URLs):** Como mapear endereços web para views usando `urls.py`.
6.  **Painel de Administração:** Como usar o `admin.py` para registrar modelos e gerenciar dados através da interface administrativa do Django.
7.  **Arquivos Estáticos:** Como servir arquivos CSS, JavaScript e imagens a partir da pasta `static/`.
8.  **Ambientes Virtuais (Virtual Environments):** A importância de usar `venv/` para isolar as dependências do projeto.
9.  **Migrações de Banco de Dados:** Como gerenciar alterações no esquema do banco de dados usando `makemigrations` e `migrate`.
10. **Configurações do Projeto:** Como o `settings.py` controla o comportamento global do projeto.

Este `README.md` serve como um guia rápido para entender a estrutura e os principais componentes deste projeto Django.