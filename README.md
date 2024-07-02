
# Poject of blogs

## Requirements

- Docker
- python
- django
- elasticsearch
- django-elasticsearch-dsl

## Exemple

```bash
cd ~/Desktop/Project_blog 
```

Create a new virtual environment in that directory

```bash
python -m pip install virtualenv 
virtualenv test
```

Activate virtual environment

```bash
source test\Scripts\activate
```
Install django 

```bash
pip install django
```

Clone the project then Go to the repository of our project

```bash
clone https://github.com/anismkb/Project_blog.git
cd multilang_site
```

Run Docker

```bash
docker compose up
```

Now open your browser and go to this address

http://localhost:9200/

### Run the project

command line to run the project 

```bash
python manage.py runserver
```

Now open your browser and go to this address

http://127.0.0.1:8000/main