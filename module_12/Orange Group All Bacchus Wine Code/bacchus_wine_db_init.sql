/*
    Title: bacchus_wine_db_init.sql
    Author: Orange Group
    Date: 12/3/2022
    Description: bacchus wine databse initialization SQL script
*/

DROP DATABASE IF EXISTS bacchus_wine;
CREATE DATABASE bacchus_wine;
DROP USER IF EXISTS 'bacchus_user'@'localhost';
CREATE USER 'bacchus_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'mysqltest';
GRANT ALL PRIVILEGES ON bacchus_wine.* TO 'bacchus_user'@'localhost';
