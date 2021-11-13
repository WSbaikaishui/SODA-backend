from django.urls import path

from SODA.views import *



urlpatterns = [
    path('login', do_login),
    path('register', do_register),
    # path('camera/list', camera_list),
    path('api/distribution', distribution),
    path('api/get_predict_list',get_predict_list)
    # path('forecast/list',  passenger_flow_forecast_list),
    ]