import os
import subprocess
import shutil

# Inicializar repositorio Git
subprocess.run(["git", "init"], check=True)

# Instalar dependencias si existe requirements.txt
if os.path.exists("requirements.txt"):
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

# Eliminar archivo de ejemplo si existe
archivo_ejemplo = "remove_me.txt"
if os.path.exists(archivo_ejemplo):
    os.remove(archivo_ejemplo)

# Crear un README personalizado
with open("README.md", "w") as f:
    f.write(f"# {{ cookiecutter.project_name }}\n\nGenerado con Cookiecutter 🚀\n")
