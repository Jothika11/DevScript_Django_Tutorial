# <i><b>Basics</i></b>

## Initial Steps:

- Setting up venv
    - `python -m venv venv`
    - `venv\Scripts\activate`

- Installing django
    - `pip install django`
    - <b> After Installing any major modules, do : </b>`pip freeze>requirements.txt`
    - <i> To check if module exists, use : </i> `pip show <module-name>`

## Start Project

- `django-admin startproject HandsOn` where HandsOn is name of your core project base.
- `cd HandsOn`

## Running Project 
- <b>Note: </b> `djangoa-admin runserver` 
<i>raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Requested setting DEBUG, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.</i>
- <b> Use: </b> `python manage.py runserver`
- check on <i>http://127.0.0.1:8000/</i> & <i>http://127.0.0.1:8000/admin/</i>
- Try `python manage.py  createsuperuser`

## Setting up and Connecting to MySQL Database
- Create a MYSQL connection and a database to use
- Update settings.py in core project
    - `{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_HandsOn',
        'USER': 'root',#MYSQL_USER,
        'PASSWORD': 'pa13ll03avi99',#MYSQL_PASSWORD,
        'HOST': '127.0.0.1',#MYSQL_HOST,
        'PORT': '3306'
        }`
- `pip install mysqlclient`
- `python manage.py showmigrations`
- `python manage.py makemigrations`
- `python manage.py migrate`
- Check the database for applied changes. `SELECT * FROM django_handson.auth_user;`

# <i><b>App and Views</i></b>

## Create New app
- `python manage.py startapp <app-name>`
- Update installed Apps in core-project's settings.py
- Include the urls of your app like : <i>path('home/', include('core.urls'))</i>

## Creating Views
- Simplest View Example <br>
<i>
def hey(request):
    return HttpResponse("Hello")
</i>
- Accomodating anonymous nestings<br>
    - Views<br>
    <i>
    def hey(request,person):
        return HttpResponse(f"Hello {person}")
    </i>
    - URL <i>path("<str:person>",hey )</i>

## Templating
- <b>static</b> folder must contain all your css, js , img and other such sources
- <b>templates</b> folder contains all your html files

    ### Jinja Templating
    - To load static folder in html files `{% load static %}
    - Add static files, like: <i> rel="stylesheet" href="{% static 'css/normalize.min.css' %}" </i>
    - The jinja blocks :<b><i>{%block footer %}{% endblock %}</i></b>
    - To extend a template in child template : <i><b>{% extends "index.html" %} {% block header %}</b><i>
    - To add href attributes, use `{% url 'view-url-name' %}`