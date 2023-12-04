# Uso de Python y Poetry para seguridad y mantenimiento 

## Instrucciones

### Iniciar entorno virtual
```commandline
python -m venv pypoetry-venv
```
### Verificar inicio de entorno virtual
```commandline
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
```commandline
source venv/bin/activate
```
## Instalar paquetes necesarios

Una vez que el entorno virtual esté activado, puedes instalar los paquetes necesarios para el proyecto:
```commandline
pip install -r requirements.txt
```
* ``` requirements.txt ``` corresponde a los paquetes a instalar

Tambien se puede generar el archivo ``` requirements.txt ``` para compatibilidad con otros sistemas, de la siguiente forma:
```commandline
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
```commandline
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
```commandline
poetry install
```
Esto instalará los paquetes especificados en el archivo ``` pyproject.toml ```.

* Tambien se puede agregar dependencias con el comando ``` poetry add ```


## Integración ReactJS + NextJs en Django + Python

### Crear proyecto Django
```commandline
django-admin startproject pypoetry_reactnextjs
```
### Crear aplicación Django
Para crear la aplicación Django debe  ingresar al folder ```pypoetry_reactnextjs```, y ejecutar el comando:

```commandline
cd pypoetry_reactnextjs
python manage.py startapp pypoetry_reactnextjsapp
```
## Configuración de Backend

1. Instalar Django CORS headers
```commandline
pip install django-cors-headers
```
2. Configurar CORS
Agregar propiedades CORS al archivo ````settings.py````
```
INSTALLED_APPS = [
    # ...
    'corsheaders',
    'pypoetry_reactnextjsapp',
]

MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    # ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # o la URL del frontend
]
```

## Configuración de Frontend

1. Crear entorno React+NextJs
````commandline
npx create-next-app@latest
````
Con este comando se despliega en la terminal un menu de configuración como el que se muestra a continuación:

```
What is your project named? pypoetry_reactnextjs_frontend
Would you like to use TypeScript? No / Yes
Would you like to use ESLint? No / Yes
Would you like to use Tailwind CSS? No / Yes
Would you like to use `src/` directory? No / Yes
Would you like to use App Router? (recommended) No / Yes
Would you like to customize the default import alias (@/*)? No / Yes
What import alias would you like configured? @/*
```
2. Configuración de Django **'whitenoise'** para manejo de archivos estaticos

Nota:_Este paso puede omitirse según los archivos a servir._
```commandline
pip install whitenoise
```




