# Instalación y actualizacion Python

Instalación

```sh
apt update
sudo apt update
sudo apt -y upgrade
```
Verificar Instalación de python
```sh
python3 -V
```
Instalación de gestor de paquetes de dependencias
```sh
sudo apt insstall -y python3-pip
```
Dependencias en entorno profesional
```sh  
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

Verificar donde esta python y pip
```sh
which python3
which pip3
```
# Entornos Virtuales

Si estas en linus o wsl debes instalar
```sh
sudo apt install -y python3-venv
```
Poner cada proyecto en su propio ambiente, entrar en cada carpeta.
```sh
python3 -m venv env
```
Activar el ambiente
```sh
source env/bin/activate
```
Salir del ambiente virtual
```sh
deactivate
```
Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo
```sh
pip3 install matplotlib==3.5.0
```
Verificar las instalaciones
```sh
pip3 freeze
```
Actualizar el documento que contiene las librerias
```sh
pip3 freeze > requirements.txt
```

# Instalacion de fastapi y uvicorn 

Navegar a proyecto Web
```sh
cd ../web-server
```

Activar ambiente del proyecto
```sh
source env/bin/activate 
```

Agregar nuevas librerías FastAPI
```sh
pip3 install fastapi
```

Agregar ASGI (Asynchronous Server Gateway Interface) Uvicorn
```sh
pip3 install "uvicorn[standard]"
```

Verificar librerías instaladas
```sh
pip3 freeze
```

Actualizar Requirements
```sh
pip3 freeze > requirements.txt
```


# Ejemplo de Docker
    
Supongamos que estás trabajando en un proyecto de aplicación web con un equipo de desarrolladores.
Cada desarrollador tiene su propia computadora y cada uno está utilizando un sistema operativo 
diferente (Windows, MacOS o Linux). Además, cada uno de ellos tiene diferentes versiones de las
herramientas y bibliotecas necesarias para desarrollar la aplicación.

Con Docker, puedes crear un contenedor que incluya todo lo necesario para ejecutar la aplicación, 
incluyendo el código, las herramientas y las bibliotecas. Luego, cada desarrollador puede ejecutar
la aplicación en su propia computadora simplemente instalando Docker y ejecutando el contenedor. 
De esta manera, cada uno de los desarrolladores puede trabajar en el mismo entorno, sin importar 
el sistema operativo o las herramientas que tenga instaladas.

Cuando esté lista para desplegar la aplicación en producción,puedes subir el contenedor 
a un repositorio de Docker y luego  ejecutarlo en cualquier servidor que tenga Docker instalado. 
De esta manera, puedes asegurarte de que la aplicación funcione de la misma manera en todos
los entornos, desde el desarrollo hasta la producción.

# Automatizando la vinculacion de archivos en Docker

Cuando realizamos un cambio en el codigo del programa, este no se refleja en el codigo almacenado 
en el contenedor por lo que para verlo reflejado debemos salir del contenedor y lanzarlo 
nuevamente lo cual daña la experiencia de desarrollo.

Para resolver este problema y ver los cambios reflejados de manera automatica en el contenedor, 
salimos del mismo y se agrega la siguiente linea en el archivo docker-compose.yml
     
```yml
services:
app-csv:
    build:
    context: .
    dockerfile: Dockerfile
    volumes:
    - .:/app
```

Una vez agregado, lanzamos el docker nuevamente con el comando:
```sh
docker-compose up -d
```

Nos conectamos con el contenedor
```sh
docker-compose exec app-csv bash
```
Y veremos los cambios que se hagan en el codigo en automatico

# Dockenizando Web Services:

Agrega los siguientes archivos en el proyecto web services

Archivo Dockerfile

```Dockerfile
FROM python:3.10 
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```
Archivo docker-compose.yml
```yml
services:
web-server:
    build:
    context: .
    dockerfile: Dockerfile
    volumes:
    - .:/app
    ports:
    - '80:80'
```

Luego, ir a la terminal y construir el contenedor con el siguiente comando

Construir el contenedor
```sh
docker-compose build
```
Lanzar el contenedor
```sh
docker-compose up -d
```
Ver el estado del contenedor
```sh
docker-compose ps
```

Finalmente, abrimos localhost en Google y verificamos que arroje lo que esperamos.
