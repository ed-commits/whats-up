# Setup

## Python Virtual Environment

### Creation

Create a virtual env called webapp-env:

`python -m venv webapp-env`

Note that if you move the git repo you will have to delete the webapp-env dir and re-create it.

## Activation

Active the virtual environment:

`source webapp-env/bin/activate`

### Installing dependencies

`pip install django`

### Running the development server

Move into the web app directory `cd whatsup`

`python manage.py runserver`

If you need to connect to it across a local network during development you can bind listen like so:

`python manage.py runserver 0.0.0.0:8000`

and then add your local ip to `ALLOWED_HOSTS` in `whatsup/settings.py`.

## Test Data

The superuser `root:root` was created for testing. (via `python manage.py createsuperuser`)
