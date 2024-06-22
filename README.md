# Prueba Técnica Desarrollo Web

Este proyecto consiste en una aplicación web para gestionar los préstamos de libros realizados por estudiantes en la Institución Universitaria Pascual Bravo. La aplicación permite registrar estudiantes, libros y préstamos, con el objetivo de mantener un control eficiente de los recursos bibliográficos.

## Pasos para configurar y ejecutar el proyecto

### Clonar el Repositorio

1. **Clonar el repositorio desde GitHub:**

   ```bash
   git clone https://github.com/qdobyte/prestamos.git
   cd prestamos



  
## Descarga e instalación del proyecto

Para descargar el proyecto puedes clonar el repositorio:

    git clone https://github.com/j2logo/tutorial-flask.git
    

### Variables de entorno

Se requiere configurar las varibles de entorno de su servidor de base de datos:

#### Linux/Mac

    FLASK_APP=app.py
    FLASK_ENV=development
    SQLALCHEMY_DATABASE_URI=mysql://usuario:password@localhost/biblioteca

#### Windows

    FLASK_APP=app.py
    FLASK_ENV=development
    SQLALCHEMY_DATABASE_URI=mysql://usuario:password@localhost/biblioteca
    
> Mi recomendación para las pruebas es que añadas esas variables en el fichero "activate" o "activate.bat"
> si estás usando virtualenv
 
### Instalación de dependencias

En el proyecto se distribuye un fichero (requirements.txt) con todas las dependencias. Para instalarlas
basta con ejectuar:

    pip install -r requirements.txt

## Ejecución con el servidor que trae Flask

Una vez que hayas descargado el proyecto, creado las variables de entorno e instalado las dependencias,
puedes arrancar el proyecto ejecutando:

    flask run
