from django.urls import path

from SODA.views import *



urlpatterns = [
    path('login', do_login),
    path('register', do_register),
    ]