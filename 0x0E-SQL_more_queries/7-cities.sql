-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
       id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
       state_id INT NOT NULL,
       name VARCHAR(256),
       CONSTRAINT states_cities_fk FOREIGN KEY (state_id) REFERENCES states(id)
       );