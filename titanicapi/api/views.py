
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

import json
from .functions import classify_passenger, load_model

class get_classification(APIView):

  def post(self, request):

    model = load_model('./titanic_model.pk')
    data = request.data
    prediction = classify_passenger(model = model, data = data)

    return(Response(prediction))