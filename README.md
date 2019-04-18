# 🛳 titanic-django

A simple example of how Django can be used to serve predictions through an API.

# ▶️ Quickstart

  

## 🐍 Create environment

  Open up a terminal in the repositories root and run these commands to align your environment:

``` conda create -n titanic-django ```

  

``` conda activate titanic-django ```

  

``` conda install --file requirements.txt ```

  
  

## 🚀 Run local Django server

This will host the API.

- Open a terminal and navigate to the titanicapi project folder (first level, not the second). Then run:

  

``` conda activate titanic-django ```

  

(making sure you are executing from within the new environment)

  

Next run

  

``` python manage.py runserver ```

  

This will run a local development server of the django app. The model's API is now ready to call!

  

## 📲 Call the API

  

- Run demo.ipynb in the titanic-django conda environment once more (or any environment with requests and pandas installed)

  

- You should be getting results from your server!

  

That's it! Congrats on your first Django model API!

  
  

## ⛏ How to build a similar django project from scratch

 

- Run the following in your desired project directory:

  

``` django-admin startproject titanicapi ```

  

``` python manage.py migrate ```

  

``` django-admin startapp api ```

  

- Add api to installed apps in main settings

  

- Add two files to api app directory:

  

1. functions.py

- here you write your functions for loading the serialized model and classifying passengers

2. urls.py

- here you specify the URL on which your API will sit. This will allow you to send post requests with feature data to get predictions.

  

- Create APIView class in view.py with a post function to handle post requests. E.g.

  

```get_classification(APIView)```

  

- Add api urls to project root urls (titanicapi/urls.py) so that the main app knows that the api urls exist. E.g.

  

``` path('api/', include('api.urls')) ```

- Try running your server to see if it likes your setup. Generally Django logs are very good.

``` python manage.py runserver ```