from django.urls import path
from . import views

urlpatterns = [
    path('classification/', views.get_classification.as_view()),
]
