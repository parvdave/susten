from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
from django.utils.translation import gettext
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class TreeHacksUser(models.Model):
    username = models.CharField(max_length=200,default="")
    food_score = models.FloatField()
    transport_score = models.FloatField()
    consumption_score = models.FloatField(default = 0.0)

    levels = models.IntegerField(default=1)
    points = models.IntegerField(default=0)

    # Specify unique related_name values for groups and user_permissions fields
    groups = models.ManyToManyField(
        Group,
        verbose_name=gettext('groups'),
        blank=True,
        related_name='susten_users_groups',  # Unique related_name for groups
        related_query_name='susten_user_group',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name= gettext('user permissions'),
        blank=True,
        related_name='susten_users_permissions',  # Unique related_name for user_permissions
        related_query_name='susten_user_permission',
    )

class Message(models.Model):
    user_id = models.CharField(max_length = 100, blank=True)
    text = models.CharField(max_length=2000,blank=True)
    isRequest = models.BooleanField(default=True)
    create_time = models.BigIntegerField()
    create_date = models.CharField(max_length=100,blank=True)
    score = models.FloatField(default=0.0)

class Score(models.Model):
    user_id = models.CharField(max_length = 100, blank=True)
    score = models.FloatField(null=False)
    intent = models.CharField(max_length=50,blank=True)

class Store(models.Model):
    store_username = models.CharField(max_length=200,unique=True,default="")
    name = models.CharField(max_length=2000, blank = True)
    rating = models.FloatField(validators=
                               [MinValueValidator(0.0),MaxValueValidator(5.0)])
    location = models.CharField(max_length=2000,blank=True)
    picture = models.CharField(max_length=2000,blank=True)
    contact = models.CharField(max_length=2000,blank=True)

class Item(models.Model):
    name = models.CharField(max_length=2000, blank=True)
    cost = models.FloatField(default=0.0)
    store_id = models.CharField(max_length=200,blank=True)
    item_type = models.FloatField(max_length=2000,blank=True)

class Order(models.Model):
    store_username = models.CharField(max_length=2000,blank=True)
    username = models.CharField(max_length=200,blank=True)
    cost = models.FloatField(default=0.0)

class OrderItem(models.Model):
    order_id = models.IntegerField(null=False)
    item_id = models.IntegerField(null=False)