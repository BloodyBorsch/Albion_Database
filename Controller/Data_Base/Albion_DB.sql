USE albion_db;
CREATE TABLE IF NOT EXISTS users (id int AUTO_INCREMENT,
            name varchar(32),
            password varchar(32),
            email varchar(32), PRIMARY KEY (id));
CREATE TABLE IF NOT EXISTS resources (id int AUTO_INCREMENT,
            name varchar(32),
            tier varchar(32),
            cost varchar(32), PRIMARY KEY (id));
SHOW TABLES;
SELECT * FROM users;

