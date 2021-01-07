import pickle

import numpy as np
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import OnlineShoppersIntentions
from .serializers import OnlineShoppersIntentionsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from .field_choices import MonthNumber, VisitorTypeNumber


@api_view(['GET', 'POST'])
def intention_list(request):
    if request.method == 'GET':
        intentions = OnlineShoppersIntentions.objects.all()
        serializer = OnlineShoppersIntentionsSerializer(intentions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OnlineShoppersIntentionsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def intention_detail(request, pk):
    try:
        intention = OnlineShoppersIntentions.objects.get(pk=pk)
    except OnlineShoppersIntentions.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OnlineShoppersIntentionsSerializer(intention)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OnlineShoppersIntentionsSerializer(intention, data=data)
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
