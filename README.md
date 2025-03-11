# Proyecto Django con Django REST Framework y MySQL

Este proyecto utiliza **Django** junto con **Django REST Framework** para construir una API RESTful, y **MySQL** como sistema de gestión de base de datos.

## Pasos para la instalación y configuración

1. **Instalar MySQL, MySQL Workbench y Configurar las Variables de Entorno**

    - **Instalar MySQL**:  
      Descarga e instala MySQL desde [aquí](https://dev.mysql.com/downloads/installer/).  
      Durante la instalación, selecciona **MySQL Server** y **MySQL Workbench**.

    - **Instalar MySQL Workbench**:  
      Si no lo instalaste junto con MySQL, puedes descargarlo de [aquí](https://dev.mysql.com/downloads/installer/).

    - **Configurar las Variables de Entorno**:  
      Asegúrate de que MySQL esté en tu `PATH` para poder usar los comandos MySQL desde la terminal.
      
        En **Windows**:
        1. Ve a **Sistema > Configuración avanzada del sistema > Variables de entorno**.
        2. Añade la carpeta `bin` de MySQL al `PATH` (por ejemplo: `C:\Program Files\MySQL\MySQL Server X.X\bin`).
        
        En **macOS/Linux**:
        Abre tu terminal y añade la ruta de MySQL al `PATH` en el archivo `~/.bash_profile` o `~/.zshrc`:
        ```bash
        export PATH=$PATH:/usr/local/mysql/bin
        ```
        Recarga el archivo de configuración con:
        ```bash
        source ~/.bash_profile  # o ~/.zshrc
        ```

2. **Crear el Entorno Virtual**

    - Navega al directorio de tu proyecto.
    - Ejecuta el siguiente comando para crear el entorno virtual:
    ```bash
    python -m venv venv
    ```
    
    - Para activar el entorno virtual:
        - En **Windows**:
        ```bash
        venv\Scripts\activate
        ```
        - En **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

    Una vez activado el entorno virtual, verás el nombre del entorno en tu terminal.

3. **Instalar Dependencias**

    Con el entorno virtual activado, ejecuta los siguientes comandos para instalar las dependencias necesarias:
    ```bash
    pip install django
    pip install djangorestframework
    pip install mysqlclient
    ```

    - **Django**: El framework web de Python.
    - **Django REST Framework**: Para crear API RESTful en Django.
    - **mysqlclient**: Cliente para interactuar con MySQL desde Django.

4. **Iniciar el Proyecto Django**

    - Crea un nuevo proyecto de Django ejecutando:
    ```bash
    django-admin startproject myproject .
    ```

    - Crea una nueva aplicación (por ejemplo, `core`) ejecutando:
    ```bash
    python manage.py startapp core
    ```

5. **Configurar la Base de Datos MySQL**

    - En el archivo `settings.py`, configura la base de datos para usar MySQL en lugar de la base de datos SQLite predeterminada. Modifica la sección `DATABASES` como sigue:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario_mysql',
            'PASSWORD': 'tu_contraseña_mysql',
            'HOST': 'localhost',  # o la IP de tu servidor MySQL
            'PORT': '3306',  # El puerto predeterminado de MySQL
        }
    }
    ```

    Asegúrate de reemplazar `nombre_de_tu_base_de_datos`, `tu_usuario_mysql` y `tu_contraseña_mysql` con la configuración correspondiente de tu MySQL.

    - Crea la base de datos en MySQL. Abre **MySQL Workbench** o la terminal de MySQL, conéctate a tu servidor MySQL y crea la base de datos:
    ```sql
    CREATE DATABASE nombre_de_tu_base_de_datos;
    ```

6. **Migraciones y Configuración de las Apps en Django**

    - En el archivo `settings.py`, encontrarás una lista llamada `INSTALLED_APPS`. Añade tu aplicación (`core`, en este caso) y cualquier otra app que estés utilizando:
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',  # Añade esta línea para Django REST Framework
        'core',  # Tu aplicación personalizada
    ]
    ```

    - Genera las migraciones necesarias para crear las tablas en la base de datos:
    ```bash
    python manage.py makemigrations
    ```

    - Aplica las migraciones a la base de datos para crear las tablas correspondientes:
    ```bash
    python manage.py migrate
    ```

7. **Ejecutar el Servidor de Desarrollo**

    Para iniciar el servidor de desarrollo de Django y probar que todo esté funcionando correctamente, ejecuta:
    ```bash
    python manage.py runserver
    ```

    Ahora deberías poder acceder al proyecto desde `http://127.0.0.1:8000/` en tu navegador.

### Notas Importantes

- **Migraciones**: Cuando crees o modifiques modelos en tu aplicación, recuerda ejecutar `makemigrations` y luego `migrate` para actualizar la base de datos.
- **MySQL**: Si cambias la configuración de la base de datos, asegúrate de que los permisos y el acceso estén correctamente configurados en MySQL.
- **Agregando Apps**: Si quieres agregar más aplicaciones al proyecto, simplemente crea una nueva app con `startapp` y luego añádela a `INSTALLED_APPS` en `settings.py`.

8. **Enlace a Video Explicativo**

Aquí tienes un enlace a un video que te explica cómo configurar un proyecto Django con MySQL:
- [Configuración de Django con MySQL](https://www.youtube.com/watch?v=7zKjqw7w7yM)

---# Proyecto

Este proyecto sigue una estrategia de ramas basada en GitFlow.

## Flujo de trabajo

1. **Crear ramas desde `develop`:**
   - Siempre que vayas a trabajar en una nueva funcionalidad o corrección, crea una rama desde `develop`.
   - El nombre de la rama debe ser descriptivo, por ejemplo: `feature/nueva-funcionalidad` o `bugfix/correccion-error`.

2. **Subir cambios a la rama remota:**
   - Una vez hayas realizado tus cambios y los hayas probado localmente, sube los cambios a la rama remota correspondiente. 
   - Usa el siguiente comando para subir tus cambios:
     ```bash
     git push origin nombre-de-tu-rama
     ```

3. **Hacer pull a `master`:**
   - Cuando todos los cambios de tu rama hayan sido aprobados y estén listos para ser integrados, realiza un 





