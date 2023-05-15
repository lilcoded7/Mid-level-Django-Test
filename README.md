# Mid-level-Django-Test
mid level python test with django

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Commands](#commands)
* [App endpoints](#app-endpoints)
* [API Documentation](#api-documentation)

## General info
Mid Level Python Test

## Technologies
* Python
* Django
* Django Rest Framework
* Beauliful Soup
* Selenium
* SQlite3

### Setup
## Installation on Linux, Mac OS and Windows
* Clone project from the develop branch
```
git clone -b develop https://github.com/coupcode/Faithom-Django-Backend.git
```

* To create a normal virtualenv (example .venv) and activate it (see Code below).

  ```
  virtualenv --python=python3.10.6 .venv
  
  . .venv/bin/activate

  (.venv) $ pip install -r requirements.txt

  (.venv) $ python manage.py makemigrations

  (.venv) $ python manage.py migrate

  (.venv) $ python manage.py createsuperuser 

  (.venv) $ python manage.py runserver
  ```

* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at http://0.0.0.0:8000).
* Open the address in the browser


## API Documentation
http://127.0.0.1:8000/api/v1/run-scraper/
```
http://127.0.0.1:8000/api/v1/records/

