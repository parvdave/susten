from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import *
import json
from datetime import datetime
from . import sustainability_model as sm
from . import calculator_model as cm
from django.contrib.auth import authenticate, login

# Create your views here.
def get_scores(response):
    print(response.user.username)
    susten_user = TreeHacksUser.objects.filter(username=response.user.username)
    if susten_user.exists():
        susten_user_object = susten_user.first()
        scores = {
        'food_score': susten_user_object.food_score,
        'transport_score': susten_user_object.transport_score,
        'consumption_score': susten_user_object.consumption_score,
        }

        return JsonResponse(scores)
    else:
        print("error")
    

    print(scores)

@csrf_exempt
def message_action(request,user_id):
    if request.method == 'GET':
        # Handle GET request
        messages = Message.objects.order_by('-create_time').filter(user_id=user_id)
        data = serialize('json', messages)
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        # Handle POST request
        data = json.loads(request.body)
        text = data.get("text")
        create_time = int(round(datetime.now().timestamp() * 1000))
        # print(text)
        response = sm.generate_response(text)

        serialized_payload = {
            'text': text,
            'user_id': user_id,
            'createTime': create_time,
            'response': response
        }
        
        handle_message_creation(user_id,text,create_time,response_text=response)

        return JsonResponse(serialized_payload)

def handle_message_creation(user_id,text,create_time,response_text):
    # intent = "fetched from LLM"
    messages = Message.objects.order_by('-create_time').filter(user_id=user_id,isRequest=True)[:10]
    historical_context = []
    for message in messages:
        historical_context.append(message.text)
    print(historical_context)
    response = cm.calculate_score(text,historical_context)
    rating_score = 0
    flag = False
    for i in response:
        if i.isnumeric():
            if flag:
                rating_score += i
                flag = False
            else:
                flag = True
    

    print(response)
    score = 0
    create_date = datetime.fromtimestamp(create_time / 1000.0)
    print("create_date=",create_date)
    response_msg = Message(text=response_text,user_id=user_id
                           ,create_date=create_date,score=0.0,isRequest=False,create_time=create_time)
    response_msg.save()
    msg = Message(text=text,user_id=user_id,create_time=create_time,score = score,create_date=create_date)
    user_obj = TreeHacksUser.objects.filter(username=user_id).first()
    user_obj.points += rating_score*10
    
    msg.save()
    handle_score_updation(user_id,score)

def handle_score_updation(user_id,recent_score):
    user_obj = TreeHacksUser.objects.filter(username=user_id).first()
    print(user_obj)
    fetching_original_score = user_obj.consumption_score
    new_count = Message.objects.filter(user_id=user_id).count()
    print(new_count)
    older_cumulative_score = fetching_original_score* (new_count-1)
    print("older cumul score=",older_cumulative_score)
    new_score = ( older_cumulative_score + recent_score ) / ( new_count )
    print("new cumul score=",new_score)
    user_obj.consumption_score = new_score
    handle_levelling_up(user_obj)
    # user_obj.save()
    print("user score updated")



def handle_levelling_up(user_obj):
    if user_obj.points > 100:
        user_obj.levels = 2
    elif user_obj.points > 500:
        user_obj.levels = 3
    user_obj.save()

def progress(request):
    treehacks_user = TreeHacksUser.objects.filter(username=request.user.username).first()
    levels = treehacks_user.levels
    level_path = f"sustenuser/levels/Level{levels}.svg"
    return render(request,'sustenuser/your_progress.html',{"treehacksuser":treehacks_user,"level_path":level_path})

def get_store(request):
    pass

def get_stores(request):
    pass

def get_items(request):
    pass

def sell_to_store(request):
    pass

def chat(request):

    return render(request, 'sustenuser/chat.html')

def user_login(request):
    if request.method == 'POST':
        print("in post if")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('chat-view')  # You can change 'home' to your desired URL
        else:
            print("in else in if")
            # Return an 'invalid login' error message.
            return render(request, 'sustenuser/login.html', {'error_message': 'Invalid login'})
    else:
        if request.user.is_authenticated:
            return redirect('chat-view')  # Redirect to home or any other desired page
        else:
            return render(request, 'sustenuser/login.html')
