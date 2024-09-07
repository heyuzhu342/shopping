from __future__ import unicode_literals
from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey(DjangoContentType, on_delete=models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(DjangoContentType, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


# 用户表
class LoginUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    email = models.CharField(max_length=255, blank=True)
    passwd = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'login_user'


# 商品表
class GoodsissueGoods(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    owner = models.ForeignKey(LoginUser, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    size = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=255, blank=True)
    introduction = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(blank=True, null=True)
    imagefile = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'goodsissue_goods'


# 商品销售表
class GoodsissueSaler(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    buyer = models.ForeignKey(LoginUser, blank=True, null=True, on_delete=models.CASCADE)
    goods_id = models.IntegerField(blank=True, null=True)
    tradedate = models.DateTimeField(db_column='tradeDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsissue_saler'


# 商品发布表
class GoodsissueIssuer(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    uid = models.ForeignKey(LoginUser, db_column='uid', blank=True, null=True, on_delete=models.CASCADE)
    goods = models.ForeignKey(GoodsissueGoods, blank=True, null=True, on_delete=models.CASCADE)
    issuedate = models.DateTimeField(db_column='issueDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsissue_issuer'
