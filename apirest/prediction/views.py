import pickle

import numpy as np
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import OnlineShopper
from .serializers import OnlineShopperSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from .field_choices import MonthNumber, VisitorTypeNumber


@api_view(['GET', 'POST'])
def shoppers_list(request):
    if request.method == 'GET':
        intentions = OnlineShopper.objects.all()
        serializer = OnlineShopperSerializer(intentions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OnlineShopperSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def shopper_detail(request, pk):
    try:
        intention = OnlineShopper.objects.get(pk=pk)
    except OnlineShopper.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OnlineShopperSerializer(intention)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OnlineShopperSerializer(intention, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        intention.delete()
        return HttpResponse(status=204)


# à voir si on peut la mettre ailleurs cette fonction
def preprocess_data(data):
    data['Month'] = MonthNumber[data["Month"]].value
    data['VisitorType'] = VisitorTypeNumber[data["VisitorType"]].value
    data.pop('Revenue')

    unit = np.array(list(data.values()))
    unit = unit.reshape(1, -1)

    return unit


@api_view(["POST"])
def buy_or_not_buy(request):
    try:
        mdl_path = "../best_model.pkl"
        mdl = pickle.load(open(mdl_path, 'rb'))

        shaped_data = preprocess_data(request.data)

        y_pred = mdl.predict(shaped_data)
        y_pred_proba = mdl.predict_proba(shaped_data)[0][0]

        df = pd.DataFrame([[y_pred, y_pred_proba]], columns=['Revenue', 'Certainty'])
        df = df.replace({True: 'Transaction', False: 'No transaction'})

        resp = f'Your Intention is : {df["Revenue"][0]} with a probability of {df["Certainty"][0]}'
        return JsonResponse(resp, safe=False)

    except ValueError as e:
        return HttpResponse(e.args[0], status=204)
