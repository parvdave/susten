from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def get_scores(response, id):
    susten_user = TreeHacksUser.objects.filter(username=id)
    if susten_user.exists():
        susten_user_object = susten_user.first()
        scores = {
        'food_score': susten_user_object.food_score,
        'transport_score': susten_user_object.transport_score,
        'consumption_score': susten_user_object.consumption_score,
        }

        return JsonResponse(scores)

    

    print(scores)



