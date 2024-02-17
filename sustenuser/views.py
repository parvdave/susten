from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import *
import json
from datetime import datetime

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

@csrf_exempt
def message_action(request,user_id):
    if request.method == 'GET':
        # Handle GET request
        messages = Message.objects.order_by('-create_time')
        data = serialize('json', messages)
        return JsonResponse(data, safe=False) 
        return JsonResponse(data)
    elif request.method == 'POST':
        # Handle POST request
        data = json.loads(request.body)
        text = data.get("text")
        create_time = int(round(datetime.now().timestamp() * 1000))
        # print(text)


        serialized_payload = {
            'text': text,
            'user_id': user_id,
            'createTime': create_time
        }
        
        handle_message_creation(user_id,text,create_time)
        return JsonResponse(serialized_payload)

def handle_message_creation(user_id,text,create_time):
    intent = "fetched from LLM"
    score = 0
    msg = Message(text=text,user_id=user_id,create_time=create_time)
    msg.save()
    handle_score_updation(user_id,score)

def handle_score_updation(user_id,recent_score):
    user_obj = TreeHacksUser.objects.filter(username=user_id).first()
    print(user_obj)
    fetching_original_score = user_obj.consumption_score
    new_count = Message.objects.filter(user_id=user_id).count() # 1
    print(new_count)
    older_cumulative_score = fetching_original_score* (new_count-1)
    print("older cumul score=",older_cumulative_score)
    new_score = ( older_cumulative_score + recent_score ) / ( new_count )
    print("new cumul score=",new_score)
    user_obj.consumption_score = new_score
    user_obj.save()
    print("user score updated")




