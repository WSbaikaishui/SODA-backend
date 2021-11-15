import request
import random
from django.core import serializers
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from SODA.models import Camera, CameraHistory, User,Scenic,PassengerFlowForecast
from SODA.serializers import PassengerFlowForecastSerializer
from django.db import connection
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

@csrf_exempt
@api_view(['POST'])
def distribution(request):
    parent_id = request.POST['parent_id']
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "select * from Distribution where scenic_parent_id = %s",(parent_id))
            data = dictfetchall(cursor)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        return Response([])

@csrf_exempt
@api_view(['POST'])
def camera_list(request):
    cameras = Camera.objects.all()
    data=set();
    for camera in cameras :
        data.add(camera.camera_id);
    if data is not None:
      return Response(data)
    else:
      return JsonResponse({'msg':'不存在摄像头'})

@csrf_exempt
@api_view(['GET'])
def get_map(request):
    camera_id = request.GET["camera_id"]
    time = request.GET["time"]
    cameraHistory = CameraHistory.objects.filter(
        camera_id=camera_id, time=time).first()
    if cameraHistory is not None:
        images = {"src": cameraHistory.picture, "createdAt": cameraHistory.time}
        imagesList = [images]
        cemeras = {"images": imagesList, "cemeraid": camera_id,
                "name": "监控点1-1号监控"}
        cemerasList = [cemeras]
        data = {"cemeras": cemerasList, "Industry": random.randint(1111111, 9999999),
                "name": random.randint(11111111, 99999999)}
        result = {"data": data,  "name": "监控点"+str(random.randint(1, 99)),
                "coordinates": [random.randint(1, 99), random.randint(1, 99)],
                "id": cameraHistory.history_id}
        return Response([result])
    else:
        return JsonResponse({'msg':'不存在摄像头数据'})



def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

@csrf_exempt
@api_view(['GET'])
def get_predict_list(request):
    scenic_id = request.GET["scenic_id"]
    scenic = Scenic.objects.filter(scenic_id= scenic_id).first()
    print(scenic)
    if scenic is not None:
        predict_list = PassengerFlowForecast.objects.filter(scenic_id=scenic_id)
        print(predict_list)
        serializer = PassengerFlowForecastSerializer(predict_list, many=True)
        return Response(serializer.data)
    else:
        return JsonResponse({'msg':'不存在此景点'})
# @csrf_exempt
# @api_view(['GET'])
# def heat_map(request):
