from django.urls import path

from SODA.views import *



urlpatterns = [
    path('login', do_login),
    path('register', do_register),
    path('camera/list', camera_list),
    path('find/all', find_all),
    path('forecast/list',  passenger_flow_forecast_list),
    ]