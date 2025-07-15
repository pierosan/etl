CREATE TABLE dim_usuario (
    id INT UNIQUE PRIMARY KEY,
    nombre VARCHAR(255),
    dni INT,
    area VARCHAR(100),
    empresa VARCHAR(100),
    fecha_creacion DATETIME,
    INDEX (nombre)
);
CREATE TABLE dim_dispositivo (
    id INT UNIQUE PRIMARY KEY,
    num_dispositivo INT,
    descripcion VARCHAR(50),
    ubicacion VARCHAR(50),
    id_nfc VARCHAR(50),
    estado VARCHAR(50),
    id_usuario INT,
    fecha_registro DATETIME,
    INDEX (descripcion),
    FOREIGN KEY (id_usuario) REFERENCES dim_usuario(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
    
);
CREATE TABLE fact_inactividad (
    id INT UNIQUE PRIMARY KEY,
    id_usuario INT,
    hora_inactividad DATETIME,
    FOREIGN KEY (id_usuario) REFERENCES dim_usuario(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
CREATE TABLE fact_reserva (
    id INT UNIQUE PRIMARY KEY,
    id_dispositivo INT,
    id_usuario INT,
    fecha_reserva DATETIME,
    motivo_reserva VARCHAR(255),
    tipo_movimiento VARCHAR(50),
    estado_dispositivo VARCHAR(50),
    FOREIGN KEY (id_dispositivo) REFERENCES dim_dispositivo(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (id_usuario) REFERENCES dim_usuario(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
CREATE TABLE fact_sesion (
    id INT UNIQUE PRIMARY KEY,
    id_usuario INT,
    tipo_cierre VARCHAR(255),
    timestamp DATETIME,
    FOREIGN KEY (id_usuario) REFERENCES dim_usuario(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
CREATE TABLE fact_ubicacion_gps (
    id INT UNIQUE PRIMARY KEY,
    id_dispositivo INT,
    timestamp DATETIME,
    latitud DECIMAL(10, 7),
    longitud DECIMAL(10, 7),
    FOREIGN KEY (id_dispositivo) REFERENCES dim_dispositivo(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);