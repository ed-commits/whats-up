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

## Test Data

The superuser `root:root` was created for testing. (via `python manage.py createsuperuser`)
