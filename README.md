# Prueba Técnica Desarrollo Web

Este proyecto consiste en una aplicación web para gestionar los préstamos de libros realizados por estudiantes en la Institución Universitaria Pascual Bravo. La aplicación permite registrar estudiantes, libros y préstamos, con el objetivo de mantener un control eficiente de los recursos bibliográficos.

## Pasos para configurar y ejecutar el proyecto

### Clonar el Repositorio

1. **Clonar el repositorio desde GitHub:**

```bash
git clone https://github.com/qdobyte/prestamos.git
cd prestamos
```

### Configurar el Entorno Virtual

2. **Crear y activar un entorno virtual:**
(Utiliza venv para crear un entorno virtual de Python)

```bash
python3 -m venv venv         # Linux/Mac
source venv/bin/activate     # Linux/Mac
```

```bash
python -m venv venv          # Windows
venv\Scripts\activate        # Windows
```
### Instalación de dependencias

3. En el proyecto se distribuye un fichero (requirements.txt) con todas las dependencias. Para instalarlas
basta con ejectuar: 
```bash
pip install -r requirements.txt
```

### Variables de entorno

4. Se debe crear un archivo .env en la raiz del proyecto
```bash
FLASK_APP=app.py
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=mysql://usuario:password@localhost/biblioteca
```

### Inicializar base de datos

5. Una vez creada la base de datos y configurado las variables de entorno se ejecutan las migraciones
```bash
flask db init
flask db migrate
flask db upgrade
```

### Ejecución con el servidor que trae Flask

Una vez que hayas descargado el proyecto, creado las variables de entorno e instalado las dependencias,
puedes arrancar el proyecto ejecutando:

```bash   
flask run
```

### Esto levantará un servidor de desarrollo y deberías ver algo como:
```bash  
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
    

 

