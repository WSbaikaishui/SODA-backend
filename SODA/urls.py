from django.urls import path

from SODA.views import *



urlpatterns = [
    path('do_login', do_login),
    path('register', do_register),
    path('api/get_camera_list', camera_list),
    path('api/get_camera_time_list', camera_time_list),
    path('api/distribution', distribution),
    path('api/get_predict_list',get_predict_list),
    path('api/get_map', get_map),
    # path('forecast/list',  passenger_flow_forecast_list),
    ]