# nexus-core

🇺🇸 English | 🇧🇷 [Português](README.md)

> A CLI that scaffolds new Django + DRF projects with Poetry, Docker, and automatic setup.

## Overview

**nexus-core** is a command-line tool (Typer) that **generates the structure of a new Django project** ready to go: it creates the project with Poetry, installs Django + Django REST Framework, registers DRF in `settings.py`, runs migrations, creates a superuser, and generates `Dockerfile` + `docker-compose.yml`.

## Commands

```bash
nexus-core info                  # project information
nexus-core startproject <name>   # create and configure a Django + DRF project
```

## Stack

Python · Typer · Poetry · Django + DRF (via subprocess) · Docker / Docker Compose.

## Running

```bash
poetry install
nexus-core info
nexus-core startproject my_project
```

## Project status

Functional prototype — main flow implemented; lacks tests and edge-case handling (e.g. existing project, configurable superuser credentials).

## License

This project does not yet declare a license. Until one is added, all rights are reserved by the author.
