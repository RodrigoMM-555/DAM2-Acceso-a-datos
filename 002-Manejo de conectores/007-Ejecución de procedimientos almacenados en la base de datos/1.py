"""
CREATE DATABASE biblioteca;

USE biblioteca;

CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100),
    ejemplares INT
);

INSERT INTO libros (titulo, autor, ejemplares) VALUES
    ('Don Quijote de la Mancha', 'Miguel de Cervantes', 3),
    ('Novelas ejemplares', 'Miguel de Cervantes', 1),
    ('La casa de Bernarda Alba', 'Federico García Lorca', 2),
    ('Romancero gitano', 'Federico García Lorca', 0);

SELECT * FROM libros;

CREATE USER 'app_biblioteca'@'localhost'
IDENTIFIED BY 'Biblio_2026';

GRANT EXECUTE ON biblioteca.* TO 'app_biblioteca'@'localhost';

USE biblioteca;

DELIMITER //

CREATE PROCEDURE listar_libros()
BEGIN
    SELECT id, titulo, autor, ejemplares
    FROM libros
    ORDER BY id;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE buscar_por_autor(IN p_autor VARCHAR(100))
BEGIN
    SELECT titulo, ejemplares
    FROM libros
    WHERE autor = p_autor
    ORDER BY id;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE contar_libros(OUT p_total INT)
BEGIN
    SELECT COUNT(*) INTO p_total
    FROM libros;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE prestar_libro(IN p_id INT)
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM libros
        WHERE id = p_id
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El libro no existe';

    ELSEIF (
        SELECT ejemplares
        FROM libros
        WHERE id = p_id
    ) = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No quedan ejemplares';

    ELSE
        UPDATE libros
        SET ejemplares = ejemplares - 1
        WHERE id = p_id;
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE prestar_libro(IN p_id INT)
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM libros
        WHERE id = p_id
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El libro no existe';

    ELSEIF (
        SELECT ejemplares
        FROM libros
        WHERE id = p_id
    ) = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No quedan ejemplares';

    ELSE
        UPDATE libros
        SET ejemplares = ejemplares - 1
        WHERE id = p_id;
    END IF;
END //

DELIMITER ;
"""
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="app_biblioteca",
    password="Biblio_2026",
    database="biblioteca"
)

cursor = conexion.cursor()


# Paso 4. Listar todos los libros

cursor.callproc("listar_libros", ())

for resultado in cursor.stored_results():
    libros = resultado.fetchall()

    print("=== Listado de libros ===")

    for id_libro, titulo, autor, ejemplares in libros:
        print(f"{id_libro} - {titulo} ({autor}) - {ejemplares} ejemplares")


# Paso 5. Buscar libros por autor

print()
print("=== Libros de Federico García Lorca ===")

cursor.callproc("buscar_por_autor", ("Federico García Lorca",))

for resultado in cursor.stored_results():
    libros = resultado.fetchall()

    for titulo, ejemplares in libros:
        print(f"{titulo} - {ejemplares} ejemplares")


# Paso 6. Contar libros

print()
print("=== Total de libros ===")

resultado = cursor.callproc("contar_libros", (0,))

print(f"Hay {resultado[0]} libros en la biblioteca")


# Paso 8. Prestar el libro 1

print()
print("=== Préstamo del libro 1 ===")

try:
    cursor.callproc("prestar_libro", (1,))
    conexion.commit()
    print("Préstamo registrado")

except mysql.connector.Error as e:
    conexion.rollback()
    print(f"Error: {e.msg}")


# Paso 8. Intentar prestar el libro 4

print()
print("=== Préstamo del libro 4 ===")

try:
    cursor.callproc("prestar_libro", (4,))
    conexion.commit()
    print("Préstamo registrado")

except mysql.connector.Error as e:
    conexion.rollback()
    print(f"Error: {e.msg}")


# Paso 9. Comprobar los permisos

print()
print("=== Prueba de permisos ===")

try:
    cursor.execute("SELECT * FROM libros")
    print("La consulta se ha ejecutado correctamente")

except mysql.connector.Error as e:
    print(f"Acceso denegado: {e.msg}")


# Cerrar el cursor y la conexión

cursor.close()
conexion.close()