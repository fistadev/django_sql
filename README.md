# Django SQL Project

- Django app 
- bootstrap front-end
- upload CSV file 
- plotly graphs
- return table of the CSV file

## Installation

Install project with pip.

Create virtual environment.
```bash
python3 -m venv venv
```

Activate virtual environment.    
```bash
. venv/bin/activate
```

Install all requirements.
```bash
pip install -r requirements.txt
```

Start running local (localhost:8000)
```python
python manage.py runserver
```

Migrations (everytime that changes models.py)
```python
python manage.py makemigrations

python manage.py migrate
```

Create superuser => add username and password
```python
python manage.py createsuperuser 
```