# Base Application Directory

Este diretório (`base`) contém os arquivos essenciais para a estrutura fundamental do nosso projeto Django. Ele é projetado para abrigar _templates_ HTML globais e arquivos estáticos (como CSS) que são comuns a toda a aplicação, garantindo consistência visual e de estrutura.

## Estrutura do Diretório

-   `global/`: Contém os _templates_ HTML que servem como base ou são partes reutilizáveis em várias páginas.
    -   `base.html`: Este é o _template_ HTML principal. Ele define a estrutura básica de todas as páginas do site, incluindo a declaração `<!DOCTYPE html>`, as tags `<html>`, `<head>` e `<body>`. Outros _templates_ irão estender este arquivo para herdar sua estrutura. É aqui que você define blocos (_blocks_) para que as páginas filhas possam inserir seu conteúdo específico.
    -   `partials/`: Este subdiretório armazena "partes" (_partials_) de HTML que são pequenas seções de código que podem ser incluídas em vários _templates_. Isso ajuda a evitar a repetição de código e a manter os _templates_ organizados.
        -   `head.html`: Provavelmente contém a seção `<head>` do HTML, onde são definidos metadados, links para folhas de estilo (CSS), títulos de página e scripts que devem ser carregados antes do corpo da página.
        -   `menu.html`: Contém o código HTML para o menu de navegação do site, que pode ser incluído em `base.html` ou em outros _templates_ que precisem de um menu.
        -   `postblock.html`: Pelo nome, sugere ser um bloco reutilizável para exibir informações de um post (como título, autor, data, um resumo). Isso seria incluído em _templates_ de listagem de posts ou páginas de categorias.

-   `static/`: Este diretório é onde o Django espera encontrar arquivos estáticos que não são processados pelo servidor, mas são servidos diretamente ao navegador do usuário.
    -   `global/`: Um subdiretório para organizar os arquivos estáticos que são globais para a aplicação.
        -   `css/`: Contém as folhas de estilo CSS.
            -   `style.css`: Esta é a folha de estilo principal do projeto, contendo as regras CSS para estilizar elementos HTML em todo o site.

## Conceitos Estudados

Para entender o funcionamento dos arquivos aqui, é importante ter conhecimento sobre os seguintes conceitos de desenvolvimento web e Django:

1.  **Django Templates:** O sistema de _templates_ do Django permite gerar HTML dinamicamente. Ele usa uma linguagem de _template_ para criar páginas que podem exibir dados do banco de dados e ter uma estrutura consistente.
2.  **Herança de Templates (Template Inheritance):** Uma funcionalidade poderosa do Django que permite que você crie um _template_ base (`base.html`) com a estrutura principal e blocos (_blocks_), e outros _templates_ (`index.html`, `post.html`, etc.) podem "estender" esse base, preenchendo apenas os blocos específicos. Isso reduz a duplicação de código e facilita a manutenção.
3.  **Inclusão de Templates (Template Includes):** A capacidade de incluir um _template_ dentro de outro (`{% include 'partials/menu.html' %}`). Isso é usado para reutilizar pequenas partes de HTML, como cabeçalhos, rodapés e menus.
4.  **Arquivos Estáticos (Static Files):** No desenvolvimento web, arquivos estáticos são aqueles que não mudam (CSS, JavaScript, imagens). Django possui um sistema para gerenciar e servir esses arquivos de forma eficiente.
5.  **CSS (Cascading Style Sheets):** A linguagem usada para estilizar elementos HTML, controlando cores, fontes, layouts e muito mais.

Ao organizar os arquivos desta forma, buscamos criar uma aplicação web que seja fácil de manter, escalável e com uma experiência de usuário consistente.
