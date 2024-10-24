Microservicios para la integración con códigos postales del Reino Unido
Este proyecto consiste en dos microservicios escritos en Python que integran la API pública de postcodes.io para obtener información de códigos postales del Reino Unido a partir de coordenadas geográficas contenidas en un archivo CSV. El entorno del proyecto está Dockerizado, y se utiliza PostgreSQL como base de datos. Los microservicios están diseñados con un enfoque en escalabilidad, separación de responsabilidades y facilidad de despliegue.

Tabla de contenidos

	•	Descripción general
	•	Arquitectura
	•	Instalación y configuración
	•	Cómo ejecutar los servicios
	•	Tecnologías utilizadas
	•	Diseño de la base de datos
	•	Endpoints de la API
	•	Manejo de errores
	•	Pruebas

Descripción general

El objetivo de este proyecto es implementar dos microservicios:

	1.	Microservicio 1: Recibe un archivo CSV con coordenadas, procesa los datos y los almacena en una base de datos PostgreSQL.
	2.	Microservicio 2: Consume la API de postcodes.io para obtener información detallada de los códigos postales más cercanos a las coordenadas proporcionadas por el Microservicio 1, y envía los resultados de vuelta para completar la información almacenada.

Ambos microservicios están Dockerizados para facilitar su despliegue, y se comunican entre sí a través de una red interna en Docker.

Arquitectura

El proyecto sigue una arquitectura de microservicios, donde cada servicio tiene una responsabilidad clara:

	•	Microservicio 1: Se encarga de recibir y procesar el archivo CSV, almacenando las coordenadas en una base de datos.
	•	Microservicio 2: Se encarga de consultar la API de postcodes.io usando las coordenadas almacenadas por el Microservicio 1, procesando la respuesta y actualizando la base de datos con los códigos postales obtenidos.

Diagrama de la arquitectura

        +--------------------+        +------------------+
        |  Microservicio 1    |        |  Microservicio 2  |
        |  (Manejo de CSV y   |        |  (Consulta API y  |
        |  almacenamiento)    |        |  actualización DB)|
        +----------+----------+        +---------+---------+
                   |                           |
                   +-----------+---------------+
                               |
                               v
                         +------------+
                         | PostgreSQL |
                         |  Database  |
                         +------------+

Flujos principales

	1.	El usuario carga un archivo CSV de coordenadas en el Microservicio 1.
	2.	El Microservicio 1 almacena las coordenadas en la base de datos.
	3.	El Microservicio 2 consulta la API de postcodes.io usando las coordenadas almacenadas y actualiza los registros en la base de datos con la información de los códigos postales.

Instalación y configuración

Requisitos previos

	•	Tener Docker y Docker Compose instalados en tu máquina.
	•	Python 3.9 o superior si deseas ejecutar localmente sin Docker (opcional).

Pasos de instalación

	1.	Clona este repositorio:

git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio


	2.	Configura el entorno de Docker con Docker Compose:

docker-compose up --build


	3.	Esto levantará dos microservicios y una base de datos PostgreSQL en contenedores de Docker. Los servicios estarán disponibles en:
	•	Microservicio 1: http://localhost:5000
	•	Microservicio 2: http://localhost:5001

Cómo ejecutar los servicios

Una vez que Docker Compose esté corriendo, puedes interactuar con los microservicios usando herramientas como Postman o curl para hacer solicitudes HTTP a los endpoints que se describen más adelante.

Detener los servicios

Para detener los servicios, usa el comando:

docker-compose down

Tecnologías utilizadas

	•	Lenguaje: Python 3.9
	•	Microservicios: Flask
	•	Base de datos: PostgreSQL
	•	ORM: SQLAlchemy
	•	Docker: Para contenedorización de los servicios
	•	Postcodes.io API: API pública para obtener información de códigos postales en el Reino Unido
	•	unittest: Para pruebas unitarias

Diseño de la base de datos

El diseño de la base de datos en PostgreSQL contiene dos tablas principales:

	1.	locations: Almacena las coordenadas que se reciben del archivo CSV.
	•	id: Clave primaria.
	•	latitude: Latitud de la coordenada.
	•	longitude: Longitud de la coordenada.
	•	postcode: Código postal obtenido del Microservicio 2.

Configuración de la base de datos

La base de datos se configura utilizando SQLAlchemy como ORM. En el archivo db.py del Microservicio 1, la base de datos PostgreSQL se conecta mediante la siguiente cadena de conexión:

DATABASE_URL = "postgresql://user:password@db:5432/postcodes_db"

Asegúrate de cambiar user y password por las credenciales correctas para tu base de datos.

Endpoints de la API

Microservicio 1

	•	POST /upload: Sube el archivo CSV con coordenadas.
	•	Body: El archivo CSV.
	•	Respuesta: Estado del procesamiento.

Microservicio 2

	•	GET /process: Procesa las coordenadas almacenadas y consulta la API de postcodes.io.
	•	Respuesta: Información de los códigos postales actualizados.

Manejo de errores

	•	Errores de formato en el CSV: Si el archivo CSV está malformado o faltan columnas, el sistema devolverá un mensaje de error detallado.
	•	Errores de la API de postcodes.io: Si la API no devuelve un código postal para una coordenada, se marcará como sin código postal en la base de datos, y se reportará en la respuesta del Microservicio 2.
	•	Errores de conexión a la base de datos: Los errores relacionados con la base de datos se manejan internamente, y el usuario recibirá un mensaje indicando el problema.

Pruebas

El proyecto utiliza unittest para realizar pruebas unitarias. Las pruebas están incluidas en los archivos test_microservice1.py y test_microservice2.py de cada microservicio.

Ejecución de pruebas

	1.	Asegúrate de estar dentro del contenedor de Docker del microservicio:

docker exec -it <nombre_del_contenedor> bash


	2.	Ejecuta las pruebas:

python -m unittest discover

Python -m unittest  test_file_handler

Python -m unittest test_services.py



Esto ejecutará todas las pruebas y mostrará los resultados en la consola.

Este README actualizado refleja el uso de unittest para pruebas, detalles de la base de datos PostgreSQL y pasos claros para desplegar y ejecutar los servicios en Docker.

