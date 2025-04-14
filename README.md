Prueba Técnica: Desarrollador de Automatizaciones y Optimización de Procesos
A continuación se describen las tres partes que comprenden la prueba técnica, cada una de ellas tiene el mismo valor en la evaluación final:

Parte 1: Procesamiento de Datos en Python
Objetivo:

Evaluar la capacidad del candidato para la consolidación y transformación de datos usando Python, con especial énfasis en la lectura, limpieza y transformación de datos desde un archivo Excel.

Instrucciones:

Descarga los archivos adjuntos "Escaneo_Prueba.xlsx" y “Grupo_Vulnerabilidades.xlsx” proporcionados.
Utilizando Python, lea los archivos y realice las siguientes transformaciones:
Estandarice la columna IP para que los datos sean de tipo string con formato x.x.x.x, donde cada x debe es un número decimal entre 0 y 255.
Crea una nueva columna Grupo generada de cruzar las tablas “Escaneo_Pruebas” y “Grupo_Vulnerabilidades” por medio del campo Gid
Genere un nuevo archivo “Escaneo_Agrupado.xlsx” donde estén agrupadas las filas por IP, Categoría y Riesgo, adicional organice por las columnas de IP y Riesgo de Alto a Bajo
Utilizando la data de “Escaneo_Agrupado.xlsx” genere un calendario para el mes de abril de 2025, remediar cada actividad (vulnerabilidad por activo, cada fila de la tabla) teniendo en cuenta las siguientes condiciones:
Primero se deben planificar las vulnerabilidades con riesgo alto, luego medio y después bajo.
El equipo de remediación trabaja de lunes a viernes
Remedian 5 actividades por día
No trabajan los festivos (Colombia)
 

Entregables:
Código fuente en Python.
Archivo "Escaneo_Agrupado.xlsx"
Calendario de remediaciones.
 

Parte 2: Uso de API REST
Objetivo:

Evaluar la capacidad para desarrollar y consumir API REST. 

Instrucciones:
Desarrolla una API REST utilizando Flask (u otro framework de tu elección) que realice las siguientes operaciones:
GET /vulnerabilidades: Retorna una lista de vulnerabilidades desde el archivo "Escaneo_Prueba.xlsx".
POST /vulnerabilidades: Permite agregar una nueva vulnerabilidad al archivo "Escaneo_Prueba.xlsx".
Crea un script en Python que consuma las siguientes operaciones de la API:
Obtiene la lista de vulnerabilidades y muestra los primeros 5 registros.
Agrega una nueva vulnerabilidad.
Entregables:
Código fuente de la API.
Script en Python que consuma la API.
Parte 3: Bases de Datos SQL
Objetivo:

Evaluar la capacidad para administrar y optimizar bases de datos.

Instrucciones:
Crea una base de datos SQL llamada "ciberseguridad".
Crea una tabla "riesgos" con la siguiente estructura:
id (INT, PRIMARY KEY, AUTO_INCREMENT)
nombre (VARCHAR, NOT NULL)
impacto (INT, NOT NULL)
probabilidad (INT, NOT NULL)
riesgo (FLOAT, NOT NULL)
Escribe un script en Python que:
Conecte a la base de datos "ciberseguridad".
Inserte los datos del archivo "Escaneo_Prueba.xlsx" en la tabla "riesgos".
Realice una consulta que retorne los riesgos con un valor de riesgo mayor a 50.
Entregables:
Script de creación de la base de datos y la tabla.
Script en Python para insertar datos y realizar la consulta.
