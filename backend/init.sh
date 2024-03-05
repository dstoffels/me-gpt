#!/bin/bash

# Load environment variables from .env file
if [ -f api/.env ]; then
    export $(grep -v '^#' api/.env | xargs)
    source api/.env
fi


echo "Creating database..."
sed "s/{{DB_NAME}}/$DB_NAME/g" db/init.sql | mysql -u $DB_USER -p$DB_PASSWORD

cd api

# Virtual Environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

source venv/Scripts/activate

echo "Installing dependencies..."
pip install -r requirements.txt

source venv/Scripts/activate

echo "Making migrations..."
python manage.py makemigrations

echo "Migrating..."
python manage.py migrate

echo "Running dev server..."
python manage.py runserver

# echo
# echo "Activate the virtual environment:"
# echo -e "\e[32m\e[4mvenv/Scripts/activate\e[0m"
# echo 

