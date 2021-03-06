# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Camera(models.Model):
    camera_id = models.AutoField(primary_key=True)
    scenic = models.ForeignKey("Scenic", on_delete=models.CASCADE)
    coordinate = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camera'


class CameraHistory(models.Model):
    history_id = models.BigAutoField(primary_key=True)
    camera = models.ForeignKey("Camera", on_delete=models.CASCADE)
    time = models.DateTimeField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camera_history'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PassengerFlowForecast(models.Model):
    id = models.AutoField(primary_key=True)
    scenic_id = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    actual_number = models.IntegerField(blank=True, null=True)
    forecast_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passenger_flow_forecast'


class Scenic(models.Model):
    scenic_id = models.AutoField(primary_key=True)
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
    scenic_id = models.IntegerField(blank=True, null=True)
    coordinate = models.CharField(max_length=30, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenic_associations'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    pass_word = models.CharField(max_length=100, blank=True, null=True)
    phone_num = models.CharField(max_length=16, blank=True, null=True)
    user_type = models.CharField(max_length=16, blank=True, null=True)
    scenic_id = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class ScenicPassengerHeatmap(models.Model):
    scenic_id = models.IntegerField(primary_key=True)
    coordinate = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    passenger_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenic_passenger_heatmap'
        unique_together = (('scenic_id', 'parent_id'),)


class Association(models.Model):
    id = models.AutoField(primary_key=True)
    scenic1 = models.ForeignKey("Scenic", on_delete=models.CASCADE)
    scenic2 = models.ForeignKey("Scenic",  related_name='user_post',on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'association'