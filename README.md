#  DJANGO-RESTful-API

Simple REST application for website about road behavior with advices and quiz about safety.

## Technology

Django REST framework, PostgreSQL


## Installing

Create a virtualenv for the project (Python 3.6+). 

Then install requirements and run server.

```
$ pip install -r requirements.txt
$ python manage.py runserver

```

After that visit `http://localhost:8000` to view the app.

## API endpoints

`[GET] /advices` - shows 50 hits from newest to older ones

`[GET] /api/v1/hits/{title_url}` - shows one hit based on the title slug.
 
 For example: 
        `title: Some title` -> 
        `title_url: some-title`

`[POST] /api/v1/hits ` - creates a new hit-entry, artistId and title are required

`[PUT] /api/v1/hits/{title_url}` - updates a hit-entry, only artist_id and title can be updated

`[DELETE] /api/v1/hits/{title_url}` - deletes selected hit

To populate datavase with fake songs and artists run fake_database.py

## Running tests

Create a virtualenv for the project (Python 3.6+). 

Install requirements with `pip install -r requirements.txt`

Run tests with `pytest`

## Word of caution

... or things to improve.

1. Tests use the same database as the locally running service does.

2. In docker, the database is a sqlite file inside the container. 
Rebuilding the container drops all data.

