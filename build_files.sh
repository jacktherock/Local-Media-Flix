# !bin/bash

# Build the project
echo "BUILD THE PROJECT"

python3.9 -m pip install -r requirements.txt 

echo "Make migrations and migrate"

python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect static"

python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
