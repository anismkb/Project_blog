
# Poject of blogs

## Requirements

- Docker
- python
- django
- elasticsearch
- django-elasticsearch-dsl

## Exemple

- cd ~/Desktop/Project_blog 

Create a new virtual environment in that directory

- python3.6 -m pip install virtualenv
- virtualenv venv -p python3.6

Activate virtual environment

- source venv/bin/activate

lancement de docker

- docker compose up

Now open your browser and go to this address

http://localhost:9200/

- command line to run your project 

python manage.py runserver

- Now open your browser and go to this address

http://127.0.0.1:8000/main