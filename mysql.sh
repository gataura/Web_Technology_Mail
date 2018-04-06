mysql -uroot -e "CREATE DATABASE qamysql;"
mysql -uroot -e "CREATE USER 'django@localhost' IDENTIFIED BY 'salikh612';"
mysql -uroot -e "GRANT ALL ON qamysql.* TO 'django@localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
