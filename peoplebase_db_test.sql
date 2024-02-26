create database if not exists peoplebase;
create user if not exists 'admin_test'@'localhost' identified by 'admin_peoplebase_test';
grant all privileges on `peoplebase`.* to 'admin_test'@'localhost';
grant select on `performance_schema`.* to 'admin_test'@'localhost';
flush privileges;