
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response

import json
from .functions import classify_passenger, load_model

class get_classification(APIView):
  def post(self, request):
    model = load_model('./api/titanic_model.pk')
    data = request.data
    prediction = classify_passenger(model = model, data = data)
    return(Response(prediction))