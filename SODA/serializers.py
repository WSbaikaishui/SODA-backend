from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from SODA.models import *
class CameraSerializer(serializers,ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'

class CameraHistorySerializer(serializers,ModelSerializer):
    class Meta:
        model =  CameraHistory
        fields = '__all__'
class PassengerFlowForecastSerializer(serializers, ModelSerializer):
    class Meta:
        model = PassengerFlowForecast
        fields = '__all_'

class ScenicSreializer(serializers, ModelSerializer):
    class Meta:
        model = Scenic
        fields = '__all__'

class ScenicAssociations(serializers, ModelSerializer):
    class Meta:
        model = ScenicAssociations
        fields = '__all__'

class User(serializers, ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
