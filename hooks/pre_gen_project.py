import re
import sys

project_name = '{{ cookiecutter.project_title }}'
author_name = '{{ cookiecutter.project_author_name }}'

if not re.match(r'^[a-zA-Z0-9\-_]+$', project_name):
    print("ERROR: El nombre del proyecto solo puede contener letras, números, guiones o guiones bajos.")
    sys.exit(1)

if len(author_name.strip()) < 3:
    print("ERROR: El nombre del autor debe tener al menos 3 caracteres.")
    sys.exit(1)
