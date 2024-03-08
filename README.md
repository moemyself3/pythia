# Pythia 🔮

Pythia is a client for an observatory database to see observation queues, alerts, and catalogs.
The client is a web-based UI using Django.

## Requirements
The database relies on PostgreSQL schemas!!
In your database you will need to setup the following schemas:

- public
- surveydb 

## Planned Features

- [x] Register Users (Django)
- [x] User Authentication (Django)
- [x] Observation Queue Dashboard
- [x] Mark field as observed
- [ ] Catalog Viewer
- [ ] Profile Manager
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
