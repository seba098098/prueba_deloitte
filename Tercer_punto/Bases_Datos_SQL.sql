-- Crear base de datos
CREATE DATABASE IF NOT EXISTS ciberseguridad;

-- Usar la base
USE ciberseguridad;

-- Crear tabla
CREATE TABLE IF NOT EXISTS riesgos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    impacto INT NOT NULL,
    probabilidad INT NOT NULL,
    riesgo FLOAT NOT NULL
);

SELECT * FROM riesgos
WHERE riesgo > 50;

