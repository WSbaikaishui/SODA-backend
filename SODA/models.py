# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Camera(models.Model):
    camera_id = models.IntegerField(primary_key=True)
    scenic_id = models.IntegerField(blank=True, null=True)
    coordinate = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camera'


class CameraHistory(models.Model):
    history_id = models.BigIntegerField(primary_key=True)
    camera_id = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camera_history'


class PassengerFlowForecast(models.Model):
    id = models.IntegerField(primary_key=True)
    scenic_id = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    actual_number = models.IntegerField(blank=True, null=True)
    forecast_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passenger_flow_forecast'


class Scenic(models.Model):
    scenic_id = models.IntegerField(primary_key=True)
    scenic_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    coordinate = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)
    capacity = models.BigIntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenic'


class ScenicAssociations(models.Model):
    id = models.IntegerField(primary_key=True)
    scenic_id = models.IntegerField(blank=True, null=True)
    coordinate = models.CharField(max_length=30, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenic_associations'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    pass_word = models.CharField(max_length=100, blank=True, null=True)
    phone_num = models.CharField(max_length=16, blank=True, null=True)
    user_type = models.CharField(max_length=16, blank=True, null=True)
    scenic_id = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
