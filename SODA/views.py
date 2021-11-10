import request

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from SODA.models import User,Scenic
# Create your views here.

@csrf_exempt
@api_view(['POST'])
def do_login(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = User.objects.filter(user_name = uname).first()
    if user.pass_word == pwd:
        return Response({'user_id': user.user_id})
    else:
        return JsonResponse({'msg': "用户名或者密码错误"})



@csrf_exempt
@api_view(['POST'])
def do_register(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    phone = request.POST['phone']
    type = request.POST['type']

    user = User.objects.filter(user_name=uname).first()
    if user is not None:
        return JsonResponse({'msg':"用户名已存在"})

    scenic = Scenic.objects.filter(scenic_id=request.POST['scenic']).first()
    if scenic is not None:
        scenic_id = scenic.scenic_id
    else:
        return JsonResponse({"msg": "景区不存在"})
    user = User(user_name = uname,
                pass_word = pwd,
                phone_num = phone,
                user_type = type,
                scenic_id = scenic_id)
    try:
        user.save(force_insert=True)
        return JsonResponse({"status": 200})
    except Exception as e:
        print(e)
        return JsonResponse({"msg": '注册错误！'})