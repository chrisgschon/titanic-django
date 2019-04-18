# 🛳 titanic-django
A simple example of using Django to serve predictions through an API.

# ▶️ Quickstart

## 🐍 Create environment

``` conda create -n titanic-django ```

``` conda activate titanic-django ```

``` conda install --file requirements.txt ```


## 🚀 Run local server to host API

- Open a terminal and navigate to the './titanicapi'

``` python manage.py runserver ```

## 📲 Call the API

- Run demo.ipynb in jupyter environment of choice (requests package the only dependancy for this part)

That's it!


## How to build the django project from scratch

``` django-admin startproject titanicapi ```

``` python manage.py migrate ```

``` django-admin startapp api ```

Add api to installed apps in main settings

Add two files to api app directory: 

functions.py
- write your functions for loading the serialized model and classifying passengers
urls.py
- specify the URL on which your API will sit. This will allow you to send post requests with feature data to get predictions.

Create APIView class in view.py with a post function to handle post requests. E.g. 

```get_classification(APIView)```



Add api urls to project root urls
