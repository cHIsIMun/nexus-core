import typer
import subprocess
import os

app = typer.Typer()

#método para retornar as informações do projeto
@app.command()
def info():
    """Show information about the project."""
    typer.echo("This is a project created by Nexus Core.")

@app.command()
def startproject(name: str):
    """Create a new Django project with the given name, initialize Poetry, and setup Django."""
    # Create the project directory
    os.makedirs(name, exist_ok=True)
    
    # Change to the project directory
    os.chdir(name)

    try:
        # Initialize Poetry in the new project directory
        subprocess.run(["poetry", "init", "--no-interaction", "--name", name], check=True)
        typer.echo("Initialized Poetry environment.")

        # Add and install Django as a dependency in the new Poetry environment
        subprocess.run(["poetry", "add", "django"], check=True)
        typer.echo("Added Django to Poetry dependencies.")


        # Add and install Django Rest Framework as a dependency in the new Poetry environment
        subprocess.run(["poetry", "add", "djangorestframework"], check=True)
        typer.echo("Added Django Rest Framework to Poetry dependencies.")

        # Create the Django project using django-admin via Poetry
        subprocess.run(["poetry", "run", "django-admin", "startproject", name+"_app" , "."], check=True)
        typer.echo(f"Successfully created Django project '{name}' within the {name} directory.")

        # Add 'rest_framework' to the INSTALLED_APPS list in the Django settings.py file
        with open(f"{name}_app/settings.py", "r") as file:
            settings = file.read()
        settings = settings.replace("django.contrib.staticfiles", "django.contrib.staticfiles',\n\t'rest_framework")
        with open(f"{name}_app/settings.py", "w") as file:
            file.write(settings)
        typer.echo("Added 'rest_framework' to the INSTALLED_APPS list in settings.py.")

        # Add a new app to the Django project
        subprocess.run(["poetry", "run", "python", "manage.py", "startapp", "core"], check=True)
        typer.echo("Added a new app named 'core' to the Django project.")

        # Migrate the database
        subprocess.run(["poetry", "run", "python", "manage.py", "migrate"], check=True)
        typer.echo("Migrated the database.")

        # Create a superuser for the Django project (admin/admin)
        subprocess.run(["poetry", "run", "python", "manage.py", "createsuperuser", "--noinput", "--username", "admin", "--email", "admin@mail.com"], check=True)
        subprocess.run([
            "poetry", "run", "python", "manage.py", "shell", "-c",
            "from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.get(username='admin'); user.set_password('asdf@1234'); user.save()"
        ], check=True)
        typer.echo("Password for superuser set successfully.")

        # Add docker-compose file to the project
        with open("docker-compose.yml", "w") as file:
            file.write(
                "version: '3'\n"
                "services:\n"
                f"  {name}:\n"
                "    build: .\n"
                "    command: python manage.py runserver\n"
                "    ports:\n"
                "      - 8000:8000\n"
                "    volumes:\n"
                "      - .:/app\n"
                "    environment:\n"
                "      - DEBUG=1\n"
                "      - SECRET_KEY\n"
            )
        typer.echo("Added docker-compose.yml file to the project.")
    
        # Add Dockerfile to the project
        with open("Dockerfile", "w") as file:
            file.write(
                "FROM python:3\n"
                "ENV PYTHONUNBUFFERED 1\n"
                "WORKDIR /app\n"
                "COPY pyproject.toml .\n"
                "RUN pip install poetry\n"
                "RUN poetry install\n"
                "COPY . .\n"
            )
        typer.echo("Added Dockerfile to the project.")

    except subprocess.CalledProcessError as e:
        typer.echo(f"Failed to complete setup: {str(e)}", err=True)
        # Optionally, clean up by removing the directory if the setup fails
        os.chdir("..")
        os.rmdir(name)
        typer.echo("Cleaned up the project directory due to failure.")

if __name__ == "__main__":
    app()
