# Aplicação `home` do Projeto Django

Esta pasta contém a aplicação `home` do projeto Django. Abaixo, descrevemos o propósito de cada arquivo principal nesta aplicação, seguindo os princípios de um MVT (Model-View-Template) framework como o Django.

## Estrutura de Arquivos

-   `__init__.py`: Indica ao Python que este diretório deve ser tratado como um pacote. Geralmente, está vazio ou contém configurações de inicialização do pacote.
-   `admin.py`: Este arquivo é usado para integrar seus modelos ao painel de administração do Django. Ao registrar um modelo aqui, você pode gerenciar os dados daquele modelo diretamente através de uma interface web amigável fornecida pelo Django.
    -   **O que aprendemos:** Como disponibilizar a administração de modelos diretamente pelo painel de controle do Django, facilitando a manipulação de dados sem escrever SQL.
-   `apps.py`: Contém a configuração da aplicação `home`. Aqui definimos o nome da aplicação (`'home'`) e outras configurações específicas, como o tipo de campo padrão para chaves primárias (`BigAutoField`), que é uma boa prática para escalabilidade.
    -   **O que aprendemos:** Como configurar uma aplicação Django, incluindo seu nome e configurações de banco de dados padrão.
-   `models.py`: Este é o coração da camada de dados da sua aplicação. Nele, você define os "modelos", que são classes Python que representam tabelas no seu banco de dados. Cada atributo da classe se torna uma coluna na tabela. Atualmente, este arquivo serve como um ponto de partida para a criação de modelos futuros.
    -   **O que aprendemos:** O conceito de Modelos no Django, que servem como a representação Python das tabelas do banco de dados, e como definir a estrutura de dados da aplicação.
-   `urls.py`: Define os padrões de URL para a aplicação `home`. Ele mapeia as URLs específicas para as funções de visualização (views) correspondentes que devem ser executadas quando essa URL é acessada.
    -   **O que aprendemos:** Como rotear requisições HTTP para funções específicas no nosso código (views) usando o sistema de URLs do Django, e como nomear URLs para fácil referência.
-   `views.py`: Contém a lógica de negócios da aplicação. As "views" são funções Python que recebem uma requisição web e retornam uma resposta. A view `home` renderiza o template `home/index.html`, passando dados para ele.
    -   **O que aprendemos:** O papel das Views como controladores que processam requisições, interagem com modelos (se existirem) e selecionam qual template será renderizado, enviando dados para ele através de um "contexto".
-   `templates/home/index.html`: Este é um arquivo de template HTML. Os templates são usados para definir a estrutura visual do que é exibido ao usuário. Este template estende um template base (`global/base.html`) e exibe conteúdo dinâmico (a variável `text` vinda da view) e um título "HOME".
    -   **O que aprendemos:** Como usar o sistema de templates do Django para criar a interface do usuário, estender templates base para reutilizar código HTML e exibir dados dinâmicos passados pelas views.
-   `__pycache__/`: Pasta gerada automaticamente pelo Python para armazenar arquivos bytecode compilados (`.pyc`), que ajudam a acelerar o carregamento do código.
-   `migrations/`: Pasta gerada pelo Django para armazenar os arquivos de migração do banco de dados. Estes arquivos descrevem as mudanças no esquema do banco de dados feitas através dos seus modelos.

## Conceitos Chave Abordados

Nesta aplicação `home`, focamos nos seguintes aspectos fundamentais do desenvolvimento web com Django:

1.  **Estrutura de Projeto e Aplicações:** Entendendo como o Django organiza o código em projetos e aplicações reutilizáveis.
2.  **MVT (Model-View-Template):** Compreendendo o fluxo de requisição-resposta no Django, onde as Views lidam com a lógica, os Templates com a apresentação e os Models (a serem desenvolvidos) com os dados.
3.  **Configuração de URLs:** Mapeando URLs para funções Python usando o `urls.py`.
4.  **Criação de Views:** Escrevendo funções em `views.py` para processar requisições e retornar respostas.
5.  **Utilização de Templates:** Renderizando HTML dinâmico com o sistema de templates do Django, incluindo herança de templates (`extends`) e uso de variáveis de contexto.
6.  **Painel Administrativo:** A base para integrar modelos ao painel administrativo do Django via `admin.py`.

Este `README.md` serve como um guia rápido para relembrar a função de cada componente e os conceitos essenciais aprendidos ao desenvolver a aplicação `home`.