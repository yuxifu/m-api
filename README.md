# Django REST framework comprehensive starting project

A starter project template to build a robust RESTful Web API using [Django REST framework](http://www.django-rest-framework.org/) .

Here is a [Live Demo](https://yuxi-m-api.herokuapp.com/) deployed at [heroku](http://heroku.com)

## Features

- Base on [django-allauth](https://github.com/pennersr/django-allauth)
- Based on [Django REST framework official tutorial](http://www.django-rest-framework.org/tutorial/quickstart/).
- Based on - Heroku [python-getting-started](https://github.com/heroku/python-getting-started).
- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.6 runtime environment. 
- [Django REST Swagger](https://django-rest-swagger.readthedocs.io/en/latest/) integration.

## How to Use

To use this project, follow these steps:

1. Create your working environment.  See [Set up Python](http://sourabhbajaj.com/mac-setup/Python/README.html).
2. Install dependences using `pip`.  
3. Download this project.
4. Run `python manage.py runserver` or `gunicorn _main.wsgi` to test.

- API root: [http://localhost:8000/](http://localhost:8000/) 
- Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

## Using Python 2.7?

Just update `runtime.txt` to `python-2.7.13` (no trailing spaces or newlines!).

## Genarating `requirements.txt`

Run `pip freeze > requirements.txt`

## Dependences

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](http://www.django-rest-framework.org/)
- [Django REST Swagger](https://django-rest-swagger.readthedocs.io/)
- [DRF Docs](http://drfdocs.com/)
- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)

## Heroku Deployment
- [Configuring Django Apps for Heroku](https://devcenter.heroku.com/articles/django-app-configuration)
- [Deploying Python and Django Apps on Heroku](https://devcenter.heroku.com/articles/deploying-python)
