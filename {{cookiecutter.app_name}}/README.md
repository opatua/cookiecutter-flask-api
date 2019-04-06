{{ cookiecutter.project_name }}
===============================

{{ cookiecutter.project_short_description}}


Quickstart
----------

Run the following commands to bootstrap your environment 

    git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
    cd {{cookiecutter.app_name}}
    pip install -r requirements/prod.txt
    cp .env.example .env

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration ::

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py run run

Now you can register and login user with parameter (email, password, and name)

    [local_server]/auth/register
    [local_server]/auth/login


Shell
-----

To open the interactive shell, run

    python manage.py shell

By default, you will have access to the flask ``app``.


Migrations
----------

Whenever a database migration needs to be made. Run the following commands ::

    python manage.py db migrate

This will generate a new migration script. Then run ::

    python manage.py db upgrade

To apply the migration.

For a full migration command reference, run ``flask db --help``.
