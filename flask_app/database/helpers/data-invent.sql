-- Active: 1759889317216@@127.0.0.1@3306@tarea2
START TRANSACTION;

-- 1) 2025-09-03 10:30 – Providencia – 7 perros, 1 mes
INSERT INTO `tarea2`.`aviso_adopcion`
(`fecha_ingreso`,`comuna_id`,`sector`,`nombre`,`email`,`celular`,
 `tipo`,`cantidad`,`edad`,`unidad_medida`,`fecha_entrega`,`descripcion`)
VALUES
('2025-09-01 10:57:00',
 (SELECT id FROM `tarea2`.`comuna` WHERE nombre='Providencia'),
 'Parque Bustamante',
 'Juana Pérez',
 'juana.perez@example.com',
 '+56 9 7777 7777',
 'perro', 7, 1, 'm',
 '2025-09-03 10:30:00',
 '7 cachorros encontrados en el parque, sanos y juguetones.'
);
SET @av1 := LAST_INSERT_ID();

INSERT INTO `tarea2`.`foto` (`ruta_archivo`,`nombre_archivo`,`aviso_id`)
VALUES ('../../static/images/pets','cachorros.jpg', @av1);

INSERT INTO `tarea2`.`contactar_por` (`nombre`,`identificador`,`aviso_id`)
VALUES ('whatsapp', '+56977777777', @av1);

-- 2) 2025-09-02 17:00 – Providencia – 3 perros, 4 años
INSERT INTO `tarea2`.`aviso_adopcion`
(`fecha_ingreso`,`comuna_id`,`sector`,`nombre`,`email`,`celular`,
 `tipo`,`cantidad`,`edad`,`unidad_medida`,`fecha_entrega`,`descripcion`)
VALUES
('2025-08-31 15:00:00',
 (SELECT id FROM `tarea2`.`comuna` WHERE nombre='Providencia'),
 'Cenco Costanera',
 'Carlos Soto',
 'carlos.soto@example.com',
 '+56 9 8888 8888',
 'perro', 3, 4, 'a',
 '2025-09-02 17:00:00',
 '3 perros adultos, dóciles y sociables.'
);
SET @av2 := LAST_INSERT_ID();

INSERT INTO `tarea2`.`foto` (`ruta_archivo`,`nombre_archivo`,`aviso_id`)
VALUES ('../../static/images/pets','american-bullys.jpg', @av2);

INSERT INTO `tarea2`.`contactar_por` (`nombre`,`identificador`,`aviso_id`)
VALUES ('instagram', '@bullys_provi', @av2);

-- 3) 2025-09-02 15:45 – Las Condes – 1 gato, 3 meses
INSERT INTO `tarea2`.`aviso_adopcion`
(`fecha_ingreso`,`comuna_id`,`sector`,`nombre`,`email`,`celular`,
 `tipo`,`cantidad`,`edad`,`unidad_medida`,`fecha_entrega`,`descripcion`)
VALUES
('2025-09-01 11:25:00',
 (SELECT id FROM `tarea2`.`comuna` WHERE nombre='Las Condes'),
  NULL,
 'Andrea Díaz',
 'andrea.diaz@example.com',
  NULL,
 'gato', 1, 3, 'm',
 '2025-09-02 15:45:00',
 NULL
);
SET @av3 := LAST_INSERT_ID();

INSERT INTO `tarea2`.`foto` (`ruta_archivo`,`nombre_archivo`,`aviso_id`)
VALUES ('../../static/images/pets','kitten.jpg', @av3);

INSERT INTO `tarea2`.`contactar_por` (`nombre`,`identificador`,`aviso_id`)
VALUES ('X', '@GatosLC', @av3);

-- 4) 2025-09-02 11:11 – Las Condes – 1 gato, 3 años
INSERT INTO `tarea2`.`aviso_adopcion`
(`fecha_ingreso`,`comuna_id`,`sector`,`nombre`,`email`,`celular`,
 `tipo`,`cantidad`,`edad`,`unidad_medida`,`fecha_entrega`,`descripcion`)
VALUES
('2025-08-27 20:11:00',
 (SELECT id FROM `tarea2`.`comuna` WHERE nombre='Las Condes'),
  NULL,
 'Felipe Rivas',
 'felipe.rivas@example.com',
 '+56 9 5555 5555',
 'gato', 1, 3, 'a',
 '2025-09-02 11:11:00',
 NULL
);
SET @av4 := LAST_INSERT_ID();

INSERT INTO `tarea2`.`foto` (`ruta_archivo`,`nombre_archivo`,`aviso_id`)
VALUES ('../../static/images/pets','gato-dormido.jpg', @av4);

INSERT INTO `tarea2`.`contactar_por` (`nombre`,`identificador`,`aviso_id`)
VALUES ('telegram', 't.me/gatos_losdom', @av4);

-- 5) 2025-08-31 19:20 – Lo Barnechea – 1 perro, 2 meses
INSERT INTO `tarea2`.`aviso_adopcion`
(`fecha_ingreso`,`comuna_id`,`sector`,`nombre`,`email`,`celular`,
 `tipo`,`cantidad`,`edad`,`unidad_medida`,`fecha_entrega`,`descripcion`)
VALUES
('2025-08-15 14:20:00',
 (SELECT id FROM `tarea2`.`comuna` WHERE nombre='Lo Barnechea'),
 'Santuario Del Valle',
 'Martina López',
 'martina.lopez@example.com',
  NULL,
 'perro', 1, 2, 'm',
 '2025-08-31 19:20:00',
 'Cachorro rescatado, necesita hogar temporal o definitivo.'
);
SET @av5 := LAST_INSERT_ID();

INSERT INTO `tarea2`.`foto` (`ruta_archivo`,`nombre_archivo`,`aviso_id`)
VALUES ('../../static/images/pets','puppy-pasto.jpg', @av5);

INSERT INTO `tarea2`.`contactar_por` (`nombre`,`identificador`,`aviso_id`)
VALUES ('whatsapp', '+56944444444', @av5);

COMMIT;
