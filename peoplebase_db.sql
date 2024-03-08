create database if not exists peoplebase;
create user if not exists 'admin'@'localhost' identified by 'admin_peoplebase';
grant all privileges on `peoplebase`.* to 'admin'@'localhost';
grant select on `performance_schema`.* to 'admin'@'localhost';
flush privileges;