#  DJANGO-RESTful-API

Simple REST application for website about road behavior with advices and quiz about safety.

## Technology

Django REST framework, PostgreSQL


## Installing

Create a virtualenv for the project (Python 3.6+). 

Apply database settings in settings,py to establish connection with your databasse.

Make migrations and migrate models to database.

Then install requirements and run server.

```
$ pip install -r requirements.txt
$ python manage.py runserver
```
After that visit `http://localhost:8000` to view the app.

## API endpoints

`[GET] /advices/` - shows 50 advices.

`[GET] /advices/<int:pk>` - shows advice with specific id.

`[GET] /quiz_questions/` - shows quiz questions.

`[GET] /users/` - shows list of users.

`[GET] /users/<int:pk>/` - shows user with specific id.

`[GET] /forum_questions/` - shows forum questions.

`[GET] /forum_questions/<int:pk>/` - shows forum question with specific id.

`[GET] /forum_answers/` - shows forum answers.

`[GET] /forum_answers/<int:pk>/` - shows forum answer with specific id.

## CRUD

`[POST] /advices/ ` - creates a new advice-entry

`[PUT] /advices/<int:pk>` - updates a advice-entry

`[DELETE] /advices/<int:pk>` - deletes selected advice

`[POST] /quiz_questions/ ` - creates a new quiz question-entry

`[PUT] /quiz_questions/<int:pk>` - updates a quiz question-entry

`[DELETE] /quiz_questions/<int:pk>` - deletes selected quiz question-entry

