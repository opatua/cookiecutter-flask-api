cookiecutter-flask-api
==================

A Flask API template for cookiecutter.

Use it now
----------

    $ pip install cookiecutter
    $ cookiecutter https://github.com/opatua/cookiecutter-flask-api.git

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.

Features
--------

- Flask-SQLAlchemy with basic User model
- User module include Register and Login
- Easy database migrations with Flask-Migrate
- Configuration in environment variables, as per [The Twelve-Factor App](https://12factor.net/config)
- Flask-Login for authentication
- Flask-Bcrypt for password hashing
- Flask's Click CLI configured with simple commands
- Utilizes best practices: [Blueprints](http://flask.pocoo.org/docs/blueprints/) and [Application Factory](http://flask.pocoo.org/docs/patterns/appfactories/) patterns 


Inspiration
-----------
- [Structuring Flask Apps](http://charlesleifer.com/blog/structuring-flask-apps-a-how-to-for-those-coming-from-django/)
- [Flask-Foundation](https://github.com/JackStouffer/Flask-Foundation) by [@JackStouffer](https://github.com/JackStouffer)
- [flask-bones](https://github.com/cburmeister/flask-bones) by [@cburmeister](https://github.com/cburmeister)
- [flask-basic-registration](https://github.com/mjhea0/flask-basic-registration) by [@mjhea0](https://github.com/mjhea0)
- [Flask Cookiecutter](https://github.com/sloria/cookiecutter-flask) by [@sloria](https://github.com/sloria)
- [Flask Official Documentation](http://flask.pocoo.org/docs/)

License
-------

MIT licensed.

Changelog
---------

0.1.0 (04/06/2019)
******************
- Initial commit
