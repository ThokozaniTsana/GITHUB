# Testprofile

testprofile is a django project that consist of 2 apps namely: polls app and user_auth app. each app has it's own urls, html files, models to mention a few.



## Installation

Installing testprofile.(for windows)
 The are few steps you need to follow:
 _Create a virtual enviroment
 python -m venv virtualenv.
 _Activate your virtualenv in order for it to be active.
 virtualenv\Scripts\Activate.
_Pip install django
_Then create project(testprofile)
django-admin startproject testprofile
_Change directory to your newly created project.
cd testprofile
_Run your project 
python manage.py runserver



    
## Usage/Examples

It is very easy to follow this project:
because it a django project, django follows model view template(MVT)
model present the data you want to see  it could be from the database, views returns relavent content and templates according to user's request and template could be an html file displaying layout of the web page and logic to display the data. To navigate your way around django provides urls, when user request urls django decides which view it will send it to. views are called based on urls requested by user.

