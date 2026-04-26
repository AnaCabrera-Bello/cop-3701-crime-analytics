#!/bin/bash

echo "Updating package list..."
sudo apt update

echo "Installing MariaDB..."
sudo apt install -y mariadb-server

echo "Starting MariaDB..."
sudo service mariadb start

echo "Installing Python dependencies..."
pip install streamlit pandas mysql-connector-python

echo "Creating database and user..."
sudo mysql <<SQL
DROP DATABASE IF EXISTS crime_analytics;
CREATE DATABASE crime_analytics;

DROP USER IF EXISTS 'crime_user'@'localhost';
CREATE USER 'crime_user'@'localhost' IDENTIFIED BY 'crimepass123';

GRANT ALL PRIVILEGES ON crime_analytics.* TO 'crime_user'@'localhost';
FLUSH PRIVILEGES;
SQL

echo "Creating database tables..."
mysql -u crime_user -pcrimepass123 crime_analytics < create_db.sql

echo "Loading sample data..."
mysql -u crime_user -pcrimepass123 crime_analytics < dataload.sql

echo "Setup complete!"
echo "Run the app with:"
echo "streamlit run app.py"
