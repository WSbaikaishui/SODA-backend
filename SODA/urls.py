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
    path('api/heat_map', heat_map),
    path('api/most_association', most_association),
    path('api/get_scenic_rank', get_scenic_rank),
    path('api/get_list', get_camera_list),
    path('api/get_association_list', get_association_list),
    path('api/get_scenic', get_scenic),
    path('api/get_association_one', get_association_one),


    # path('forecast/list',  passenger_flow_forecast_list),
    ]