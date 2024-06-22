# Prueba Técnica Desarrollo Web

Este proyecto consiste en una aplicación web para gestionar los préstamos de libros realizados por estudiantes en la Institución Universitaria Pascual Bravo. La aplicación permite registrar estudiantes, libros y préstamos, con el objetivo de mantener un control eficiente de los recursos bibliográficos.

## Pasos para configurar y ejecutar el proyecto

### Clonar el Repositorio

**Clonar el repositorio desde GitHub:**

   ```bash
   git clone https://github.com/qdobyte/prestamos.git
   cd prestamos
    

# Crear y activar el entorno virtual
   ```bash
   python3 -m venv venv         # Linux/Mac
   source venv/bin/activate     # Linux/Mac
# o
   ```bash
   python -m venv venv          # Windows
   venv\Scripts\activate        # Windows

# Configurar variables de entorno (estas deben estar en un archivo .env en la raiz del proyecto)
      FLASK_APP=app.py
      FLASK_ENV=development
      SQLALCHEMY_DATABASE_URI=mysql://usuario:password@localhost/biblioteca

### Instalación de dependencias

En el proyecto se distribuye un fichero (requirements.txt) con todas las dependencias. Para instalarlas
basta con ejectuar:

   ```bash
   pip install -r requirements.txt

# Inicializar base de datos

   ```bash
   flask db init
   flask db migrate
   flask db upgrade


## Ejecución con el servidor que trae Flask

Una vez que hayas descargado el proyecto, creado las variables de entorno e instalado las dependencias,
puedes arrancar el proyecto ejecutando:

   ```bash   
   flask run

Esto levantará un servidor de desarrollo y deberías ver algo como:
```bash  
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

    

 

