CREATE DATABASE IF NOT EXISTS peoplebase;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin_peoplebase';
GRANT ALL PRIVILEGES ON `peoplebase`.* TO 'admin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;