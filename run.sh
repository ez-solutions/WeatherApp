#!/bin/bash
DB="db.sqlite3"
if [ -f "$DB" ]
then
	echo "Resuming mysite using database: $DB"
else
	echo "Creating database..."
    python manage.py migrate
fi

echo "Retrieving weather forecasts..."
python manage.py getforecasts

echo "Migrating"
python manage.py makemigrations mysite

echo "Starting application..."
python manage.py runserver 127.0.0.1:8080