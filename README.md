# Pythia 🔮

Pythia is a client for an observatory database to see observation queues, alerts, and catalogs.
The client is a web-based UI using Django.

## Requirements
The database relies on PostgreSQL schemas!!
In your database you will need to setup the following schemas:

- public
- surveydb
- alerts

### Python and Django
This was written using Python 3.12 and Django 5.0.3.

## Installation
### Steps

1. make a virtual enviorment

We recommend you make a seperate virtual enviroment!

### Note for conda enviorments
If you use anaconda to make a conda enviorment and try to install django 
with conda you may be using an older version of django!

To use the latest version of django either use conda-forge channel or
use pip install django.

2. install Django
3. download or clone this repo
4. ``cd pythia/pythia``
5. copy ``.env.example`` and save as ``.env``
6. edit ``.env`` with your setup
    1. be sure to update parameters for your use case
7. run migrations for the database schemas seperately
    1. ``python manage.py migrate --database=django``
    2. ``python manage.py migrate --database=surveydb``
    3. ``python manage.py migrate --database=alerts``
8. optional step for admin account ``python manage.py createsuperuser``
9. ``python manage.py runserver``
10. open a browser window and visit the ip address django provides, the default is ``http://127.0.0.1:8000/``


## Planned Features

- [x] Register Users (Django)
- [x] User Authentication (Django)
- [x] Observation Queue Dashboard
- [x] Mark field as observed
- [ ] Catalog Viewer
- [ ] Profile Manager
- [ ] Broker Alert Viewer
- [ ] More...

## Known Issues

### Finding them now. Under heavy development.

## Considerations

#### Django's Development Server

As per Django [Documentation](https://docs.djangoproject.com/en/4.1/ref/django-admin/#django-admin-runserver)
> DO NOT USE THIS SERVER IN A PRODUCTION SETTING. It has not gone through security audits or performance tests. (And that’s how it’s gonna stay. We’re in the business of making web frameworks, not web servers, so improving this server to be able to handle a production environment is outside the scope of Django.)

[How to deploy Django](https://docs.djangoproject.com/en/5.0/howto/deployment/)


#### Authentication

Based on the previous section you should consider safe network practices.
