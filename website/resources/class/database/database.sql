/* 
 Tables:
 - Userlevel;
 - Users;
 - Sessions;
 
 */
CREATE DATABASE IF NOT EXISTS u134325634_sgpc;
CREATE USER IF NOT EXISTS 'u134325634_sgpc' @'localhost' IDENTIFIED BY 'nbCVThXtD5NZ9Md5@WV96sRR^2EpKc6y';
GRANT ALL PRIVILEGES ON *.* TO 'u134325634_sgpc' @'localhost';
USE u134325634_sgpc;
CREATE TABLE IF NOT EXISTS Userlevel (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS Users (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    username VARCHAR(50),
    email VARCHAR(50),
    userlevel_id INT UNSIGNED DEFAULT 1,
    areaID INT UNSIGNED DEFAULT 1,
    provaID INT UNSIGNED DEFAULT 1,
    password varchar(255),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lastchange_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    disabled BOOLEAN DEFAULT 1
);
CREATE TABLE IF NOT EXISTS Sessions (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    UserID INT UNSIGNED,
    PHPsession_id VARCHAR(255),
    UserIP VARCHAR(255),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lastchange_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS Áreas (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lastchange_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS Provas (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    areaID INT UNSIGNED,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lastchange_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS QuestõesObjetiva (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    provaID INT UNSIGNED,
    numero INT UNSIGNED,
    enunciado TEXT(10000),
    respostapre VARCHAR(1),
    respostapos VARCHAR(1),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lastchange_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS QuestõesDiscursiva (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    areaID INT UNSIGNED,
    numero INT UNSIGNED,
    enunciado TEXT(10000),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lastchange_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS NotasObjetiva (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    candidatoID INT UNSIGNED,
    notapre FLOAT,
    notapos FLOAT,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lastchange_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS RespostasDiscursiva (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    candidatoID INT UNSIGNED,
    questaonumero INT UNSIGNED,
    nota FLOAT,
    avaliacao TEXT(2000),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lastchange_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS RecursosObjetiva (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    candidatoID INT UNSIGNED,
    questaonumero INT UNSIGNED,
    justificativa TEXT(2000),
    avaliacao TEXT(2000),
    status_ VARCHAR (255),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lastchange_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS RecursosDiscursiva (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    candidatoID INT UNSIGNED,
    questaonumero INT UNSIGNED,
    justificativa TEXT(2000),
    avaliacao TEXT(2000),
    status_ VARCHAR (255),
    nota VARCHAR (255),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lastchange_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
INSERT IGNORE INTO Userlevel (id, name)
VALUES (1, "candidato"),
    (2, "banca"),
    (3, "admin"),
    (4, "master");
INSERT IGNORE INTO Users (
        id,
        username,
        userlevel_id,
        areaID,
        provaID,
        password
    )
VALUES (
        1,
        "candidato",
        1,
        1,
        1,
        "$2y$10$91dBIAPD3Hmd4B4a3NIYAukTjY0UKgDIR0O.xcMwqZx4g4fQzNyli"
    ),
    (
        2,
        "banca",
        2,
        1,
        NULL,
        "$2y$10$91dBIAPD3Hmd4B4a3NIYAukTjY0UKgDIR0O.xcMwqZx4g4fQzNyli"
    ),
    (
        3,
        "admin",
        3,
        NULL,
        NULL,
        "$2y$10$91dBIAPD3Hmd4B4a3NIYAukTjY0UKgDIR0O.xcMwqZx4g4fQzNyli"
    ),
    (
        4,
        "master",
        4,
        NULL,
        NULL,
        "$2y$10$91dBIAPD3Hmd4B4a3NIYAukTjY0UKgDIR0O.xcMwqZx4g4fQzNyli"
    );