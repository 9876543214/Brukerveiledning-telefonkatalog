-- bytt ut passord hvis ønskelig (stringen etter "IDENTIFIED BY")
-- lim inn følgende:
CREATE USER 'root'@'localhost' IDENTIFIED BY 'hemmelig'; 
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';
FLUSH PRIVILEGES;

exit;

-- logg inn i mariadb igjen med brukeren root

-- skriv inn "mariadb -u root -p"

-- det du skrev inn etter "IDENTIFIED BY" er passordet

-- skriv inn passord

-- Lim in resten:

CREATE DATABASE telefonkatalog;
USE telefonkatalog;

CREATE TABLE personer(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    fornavn VARCHAR(255) NOT NULL,
    etternavn VARCHAR(255) NOT NULL,
    telefonnummer CHAR(8) NOT NULL
);