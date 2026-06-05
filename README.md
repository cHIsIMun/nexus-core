# nexus-core

🇧🇷 Português | 🇺🇸 [English](README.en.md)

> CLI que faz *scaffolding* de novos projetos Django + DRF com Poetry, Docker e setup automático.

## Visão geral

**nexus-core** é uma ferramenta de linha de comando (Typer) que **gera a estrutura de um novo projeto Django** já configurado: cria o projeto com Poetry, instala Django + Django REST Framework, registra o DRF no `settings.py`, roda as migrations, cria um superusuário e gera `Dockerfile` + `docker-compose.yml`.

## Comandos

```bash
nexus-core info                  # informações do projeto
nexus-core startproject <nome>   # cria e configura um projeto Django + DRF
```

## Stack

Python · Typer · Poetry · Django + DRF (via subprocess) · Docker / Docker Compose.

## Como executar

```bash
poetry install
nexus-core info
nexus-core startproject meu_projeto
```

## Estado do projeto

Protótipo funcional — fluxo principal implementado; faltam testes e tratamento de casos de borda (ex.: projeto já existente, credenciais de superusuário configuráveis).

## Licença

Este projeto ainda não declara uma licença; até que uma seja adicionada, todos os direitos são reservados ao autor.
