CREATE DATABASE stanok
CREATE TABLE people (
    ID INT(100) AUTO_INCREMENT,
    login VARCHAR(20),
    status VARCHAR(3),
    course INT(6),
    fuckulty VARCHAR(30),
    sex VARCHAR(7),
    password VARCHAR(10),
    PRIMARY KEY(ID)
    );
CREATE TABLE progress (
    ID INT(100) AUTO_INCREMENT,
    login VARCHAR(20),
    course INT(6),
    fuckulty VARCHAR(30),
    physic INT(10),
    math INT(10),
    python INT(10),
    lang INT(10),
    PRIMARY KEY(ID)
    );

