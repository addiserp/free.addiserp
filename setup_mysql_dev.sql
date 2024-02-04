-- prepares a MySQL server for the projectdb
-- FREE_MYSQL_USER=free_dev FREE_MYSQL_PWD=free_dev_pwd FREE_MYSQL_HOST=localhost FREE_MYSQL_DB=free_dev_db FREE_TYPE_STORAGE=db
drop DATABASE free_dev_db;
CREATE DATABASE IF NOT EXISTS free_dev_db;
CREATE USER IF NOT EXISTS 'free_dev'@'localhost' IDENTIFIED BY 'free_dev_pwd';
GRANT ALL PRIVILEGES ON `free_dev_db`.* TO 'free_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'free_dev'@'localhost';
FLUSH PRIVILEGES;

drop DATABASE free_dev_db1;
CREATE DATABASE IF NOT EXISTS free_dev_db1;
CREATE USER IF NOT EXISTS 'free_dev1'@'localhost' IDENTIFIED BY 'free_dev_pwd1';
GRANT ALL PRIVILEGES ON `free_dev_db1`.* TO 'free_dev1'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'free_dev1'@'localhost';
FLUSH PRIVILEGES;