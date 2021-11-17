import request
import random
import time
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
    # uname = request.POST['username']
    uname = request.POST.get('username')
    pwd = request.POST.get('password')
    user = User.objects.filter(user_name = uname).first()
    if user is not None:
        if user.pass_word == pwd:
            return Response({'user_id': user.user_id})
        else:
            return JsonResponse({'msg': "用户名或者密码错误"})
    else:
        return JsonResponse({'msg': "用户名或者密码错误"})

@csrf_exempt
@api_view(['POST'])
def do_register(request):
    uname = request.POST.get('username')
    pwd = request.POST.get('password')
    phone = request.POST.get('phone')
    type = request.POST.get('type')

    user = User.objects.filter(user_name=uname).first()
    if user is not None:
        return JsonResponse({'msg':"用户名已存在"})

    scenic = Scenic.objects.filter(scenic_id=request.POST.get('scenic')).first()
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
    parent_id = request.POST.get('parent_id')
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
def camera_time_list(request):
    camera_id = request.POST.get('camera_id')
    scenic_id = request.POST.get('scenic_id')
    cameraHistoryList=[]
    if camera_id !='':
        cameraHistories = CameraHistory.objects.filter(camera_id=camera_id)
        for cameraHistory in cameraHistories :
            cameraHistoryList.append(cameraHistory)
    elif scenic_id !='' :
        CameraList = Camera.objects.filter(scenic_id=scenic_id)
        for camera in CameraList:
            cameraHistories=camera.camerahistory_set.all()
            for cameraHistory in cameraHistories :
              cameraHistoryList.append(cameraHistory)

    if cameraHistoryList is not None:
        timeList=[]
        for c in cameraHistoryList :
            timeList.append(c.time.timestamp())
        return Response(timeList)
    else:
        return JsonResponse({'msg':'不存在摄像头'})



@csrf_exempt
@api_view(['POST'])
def camera_list(request):
    camera_id = request.POST.get('camera_id')
    scenic_id = request.POST.get('scenic_id')
    timestamp = request.POST.get("time")
    cameraHistoryList=[]
    if camera_id !='':
        cameraHistories = CameraHistory.objects.filter(camera_id=camera_id)
        for cameraHistory in cameraHistories :
            cameraHistoryList.append(cameraHistory)
    elif scenic_id !='' :
        CameraList = Camera.objects.filter(scenic_id=scenic_id)
        for camera in CameraList:
            cameraHistories=camera.camerahistory_set.all()
            for cameraHistory in cameraHistories :
              cameraHistoryList.append(cameraHistory)

    if cameraHistoryList is not None:
        date=[]
        for c in cameraHistoryList :
            if timestamp=='' or float(timestamp)==c.time.timestamp() :
                ob={"max":int(c.number*1.2),"current":c.number,"position":1,"position":c.camera.coordinate,"cemareid":c.camera_id}
                date.append(ob)
        return Response(date)
    else:
        return JsonResponse({'msg':'不存在摄像头'})

@csrf_exempt
@api_view(['POST'])
def get_map(request):
    scenic_id = request.POST.get("scenic_id")
    timestamp = int(request.POST.get("time"))
    tempTime = time.localtime(timestamp)
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", tempTime)
    cameraList = Camera.objects.filter(scenic_id=scenic_id)
    chsall = set()
    for camera in cameraList:
       chs = camera.camerahistory_set.filter(time=timeStr)
       for ch in chs:
            chsall.add(ch)
    if chsall is not None:
        cemerasList = []
        for ch in chsall:
            images = {"src": ch.picture, "createdAt": timestamp}
            cemeras = {"images": images, "cemeraid": ch.camera_id,
                        "name": "监控点1-1号监控"}
            cemerasList.append(cemeras)
        data = {"cemeras": cemerasList, "Industry": random.randint(1111111, 9999999),
                "name": random.randint(11111111, 99999999)}
        result = {"data": data,  "name": "监控点"+str(random.randint(1, 99)),
                  "coordinates": [random.randint(1, 99), random.randint(1, 99)],
                  "id": scenic_id}
        return Response([result])
    else:
        return JsonResponse({'msg': '不存在摄像头数据'})



def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

@csrf_exempt
@api_view(['GET'])
def get_predict_list(request):
    parent_id = request.GET['scenic_id']
    time = []
    actual = []
    forecast = []
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "select * from predictList where scenic_id = %s", (parent_id))
            data = dictfetchall(cursor)
            for item in data:
                time.append(item['time'])
                actual.append(item['actual_number'])
                forecast.append(item['forecast_number'])
        return JsonResponse({'parent_id': parent_id,'time':time, 'actual':actual, 'forecast':forecast})
    except Exception as e:
        return Response([])

@csrf_exempt
@api_view(['POST'])
def heat_map(request):
    parent_id = request.POST.get('scenic_id')
    timestamp = int(request.POST.get("time"))
    tempTime = time.localtime(timestamp)
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", tempTime)
    sceniclist =  Scenic.objects.filter(parent_id=parent_id)
    print(sceniclist)
    scenicpointList = []
    for item in sceniclist:
        passengerflowforecast = PassengerFlowForecast.objects.filter(scenic_id=item.scenic_id).first()
        if passengerflowforecast is not None:
            print(passengerflowforecast)
        else:
            continue
        # scenicpointList.append([passengerflowforecast.scenic_id,item.coordinate,passengerflowforecast.actual_number])
    return JsonResponse({"1"})

@csrf_exempt
@api_view(['GET'])
def association(request):
    parent_id = request.get['scenic_id']
    timestamp = int(request.POST.get("time"))
    tempTime = time.localtime(timestamp)
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", tempTime)
    sceniclist =  Scenic.objects.filter(parent_id=parent_id)
    print(sceniclist)
    scenicpointList = []
    for item in sceniclist:
        passengerflowforecast = PassengerFlowForecast.objects.filter(scenic_id=item.scenic_id).first()
        if passengerflowforecast is not None:
            print(passengerflowforecast)
        else:
            continue
        # scenicpointList.append([passengerflowforecast.scenic_id,item.coordinate,passengerflowforecast.actual_number])
    return JsonResponse({"1"})

