# titanic-django
A simple illustration of how to use Django to serve your model through an API


## Create environment

``` conda create -n titanic-django ```

``` conda activate titanic-django ```

``` conda install --file requirements.txt ```

## Build

``` python manage.py runserver ```

``` python manage.py migrate ```

``` django-admin startapp api ```

Add api to installed apps in main settings

Add * to ALLOWED_HOSTS

Add files: 

functions.py
urls.py

to api app

Add api urls to project root urls











## Get API predictions
