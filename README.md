Codebloga!

This is a web application developed using Django 1.8 and Polymer 1.6 for posting code snippets. It runs on SQLite database the credentials for login is `author` and `Default` as password

### Create & Activate Virtual Environment
    $ virtualenv env
    $ source env/bin/activate

### Migrations

    $ python manage.py makemigrations
    $ python manage.py migrate

To begin, fire up a local server from inside the `codebloga` directory.

### Firing up server sing python's built in server

This command serves the app at `http://localhost:8000` and provides basic URL
routing for the app:

    $ python manage.py runserver
