-- Active: 1759889317216@@127.0.0.1@3306@tarea2
START TRANSACTION;

-- (1)
INSERT INTO `tarea2`.`aviso_adopcion`
(`fecha_ingreso`,`comuna_id`,`sector`,`nombre`,`email`,`celular`,
 `tipo`,`cantidad`,`edad`,`unidad_medida`,`fecha_entrega`,`descripcion`)
VALUES
('2025-09-01 10:57:00',
 (SELECT id FROM `tarea2`.`comuna` WHERE nombre='Providencia'),
 'Parque Bustamante',
 'Juana Pérez',
 'juana.perez@example.com',
 '+569.77777777',
 'perro', 3, 3, 'm',
 '2025-09-03 10:30:00',
 '3 cachorros encontrados en el parque, sanos y juguetones.'
);
SET @av1 := LAST_INSERT_ID();

INSERT INTO `tarea2`.`foto` (`ruta_archivo`,`nombre_archivo`,`aviso_id`)
VALUES ('../../static/images/pets','3-puppies.jpg', @av1);
INSERT INTO `tarea2`.`foto` (`ruta_archivo`,`nombre_archivo`,`aviso_id`)
VALUES ('../../static/images/pets','puppy-1.jpg', @av1);
INSERT INTO `tarea2`.`foto` (`ruta_archivo`,`nombre_archivo`,`aviso_id`)
VALUES ('../../static/images/pets','puppy-2.jpg', @av1);
INSERT INTO `tarea2`.`foto` (`ruta_archivo`,`nombre_archivo`,`aviso_id`)
VALUES ('../../static/images/pets','puppy-3.jpg', @av1);

INSERT INTO `tarea2`.`contactar_por` (`nombre`,`identificador`,`aviso_id`)
VALUES ('whatsapp', '+569.77777777', @av1);

-- (2)
INSERT INTO `tarea2`.`aviso_adopcion`
(`fecha_ingreso`,`comuna_id`,`sector`,`nombre`,`email`,`celular`,
 `tipo`,`cantidad`,`edad`,`unidad_medida`,`fecha_entrega`,`descripcion`)
VALUES
('2025-08-31 15:00:00',
 (SELECT id FROM `tarea2`.`comuna` WHERE nombre='Providencia'),
 'Cenco Costanera',
 'Carlos Soto',
 'carlos.soto@example.com',
 '+569.88888888',
 'perro', 3, 4, 'a',
 '2025-09-02 17:00:00',
 '3 perros adultos, dóciles y sociables.'
);
SET @av2 := LAST_INSERT_ID();

INSERT INTO `tarea2`.`foto` (`ruta_archivo`,`nombre_archivo`,`aviso_id`)
VALUES ('../../static/images/pets','american-bullys.jpg', @av2);

INSERT INTO `tarea2`.`contactar_por` (`nombre`,`identificador`,`aviso_id`)
VALUES ('instagram', '@bullys_provi', @av2);

-- (3)
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

-- (4)
INSERT INTO `tarea2`.`aviso_adopcion`
(`fecha_ingreso`,`comuna_id`,`sector`,`nombre`,`email`,`celular`,
 `tipo`,`cantidad`,`edad`,`unidad_medida`,`fecha_entrega`,`descripcion`)
VALUES
('2025-08-27 20:11:00',
 (SELECT id FROM `tarea2`.`comuna` WHERE nombre='Las Condes'),
  NULL,
 'Felipe Rivas',
 'felipe.rivas@example.com',
 '+569.55555555',
 'gato', 1, 3, 'a',
 '2025-09-02 11:11:00',
 NULL
);
SET @av4 := LAST_INSERT_ID();

INSERT INTO `tarea2`.`foto` (`ruta_archivo`,`nombre_archivo`,`aviso_id`)
VALUES ('../../static/images/pets','gato-dormido.jpg', @av4);

INSERT INTO `tarea2`.`contactar_por` (`nombre`,`identificador`,`aviso_id`)
VALUES ('telegram', 't.me/gatos_losdom', @av4);

-- (5)
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
VALUES ('whatsapp', '+569.44444444', @av5);

-- (6)
INSERT INTO `tarea2`.`aviso_adopcion`
(`fecha_ingreso`,`comuna_id`,`sector`,`nombre`,`email`,`celular`,
 `tipo`,`cantidad`,`edad`,`unidad_medida`,`fecha_entrega`,`descripcion`)
VALUES
('2025-08-26 13:20:00',
 (SELECT id FROM `tarea2`.`comuna` WHERE nombre='Huechuraba'),
  NULL,
 'Javiera Rojas',
 'javiera.rojas@example.com',
  '+569.12341234',
 'gato', 1, 5, 'a',
 '2025-08-30 12:00:00',
  NULL
);
SET @av6 := LAST_INSERT_ID();

INSERT INTO `tarea2`.`foto` (`ruta_archivo`,`nombre_archivo`,`aviso_id`)
VALUES ('../../static/images/pets','gato-5-annos.jpg', @av6);

INSERT INTO `tarea2`.`contactar_por` (`nombre`,`identificador`,`aviso_id`)
VALUES ('whatsapp', '+569.44444444', @av6);

-- COMMIT
COMMIT;
