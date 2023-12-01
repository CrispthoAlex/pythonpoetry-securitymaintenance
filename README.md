# Uso de Python y Poetry para seguridad y mantenimiento 

## Instrucciones

### Iniciar entorno virtual
```
>>> python -m venv [name_venv]

En este caso:
>>> python -m venv pypoetry-venv
```
### Verificar inicio de entorno virtual
```
which python
```
Si el entorno virtual está iniciado, el comando devolverá la ruta al intérprete de Python del entorno virtual. 
Por ejemplo, si el entorno virtual se llama venv, el comando devolverá algo como:
```
/home/tu_usuario/venv/bin/python
```
También puedes verificar el entorno virtual activo usando el siguiente comando:
```
echo $VIRTUAL_ENV
```
Si el entorno virtual está iniciado, el comando devolverá la ruta al directorio del entorno virtual. Por ejemplo, 
si el entorno virtual se llama venv, el comando devolverá algo como:
```
/home/tu_usuario/venv
```
Si el entorno virtual no está iniciado, el comando which python devolverá la ruta al intérprete de Python global. 
El comando ```echo $VIRTUAL_ENV``` devolverá una cadena vacía.

Si el entorno virtual no está iniciado, puedes iniciarlo con el siguiente comando:
```
source venv/bin/activate
```
## Instalar paquetes necesarios

Una vez que el entorno virtual esté activado, puedes instalar los paquetes necesarios para el proyecto:
```
pip install -r requirements.txt
```
* ``` requirements.txt ``` corresponde a los paquetes a instalar

Tambien se puede generar el archivo ``` requirements.txt ``` para compatibilidad con otros sistemas, de la siguiente forma:
```
poetry export -f requirements.txt --output requirements.txt --without-hashes
```
Inicialmente se genera un archivo que contiene una configuración similar a esta:
```
asgiref==3.7.2 ; python_version >= "3.11" and python_version < "4.0"
django==4.2.7 ; python_version >= "3.11" and python_version < "4.0"
sqlparse==0.4.4 ; python_version >= "3.11" and python_version < "4.0"
tzdata==2023.3 ; python_version >= "3.11" and python_version < "4.0" and sys_platform == "win32"
```

## Configuración con Poetry

Para configurar Poetry, puedes seguir los siguientes pasos:

1. Instala Poetry con el siguiente comando:
```
pip install poetry
```
2. Crea un nuevo archivo ``` pyproject.toml ``` en la raíz del proyecto. Este archivo contiene la configuración de 
Poetry para el proyecto.

3. En el archivo ``` pyproject.toml ```, agrega la configuración correspondiente a los paquetes necesarios:
```
[tool.poetry]
name = "pythonpoetry-securitymaintenance"
version = "0.1.0"
description = "Un e-commerce para micro-empresarios"
authors = ["Crispthofer Rincon"]

[tool.poetry.dependencies]
python = "^3.11"
django = "^4.2.0"

[tool.poetry.dev-dependencies]
pytest = "^7.4.3"
black = "^21.12b0"
isort = "^5.9.3"
```

4. Usa el siguiente comando para instalar los paquetes necesarios para el proyecto:
```
poetry install
```
Esto instalará los paquetes especificados en el archivo ``` pyproject.toml ```.

## Integración ReactJS en Django + Python + NextJs
