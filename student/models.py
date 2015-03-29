from django.db import models
from django.db.models import AutoField
from djangotoolbox.fields import ListField, EmbeddedModelField
from django_mongodb_engine.contrib import MongoDBManager

# Create your models here.
class UserAccount(models.Model):
    id = AutoField('primary key', primary_key=True)
    name = models.CharField('Name', max_length=500, blank=True)
    age = models.IntegerField('Age', null=True, blank=True)
    class = models.CharField('Class', max_length=500, blank=True)

    objects = MongoDBManager()

    class Meta:
        db_table = 'useraccount'


class Attendence(models.Model):
    id = AutoField('primary key', primary_key=True)
    user = models.ForeignKey('UserAccount', verbose_name="user object")
    date = models.DateTimeField('activity date')

    objects = MongoDBManager()

    class Meta:
        db_table = 'attendence'


class Points(models.Model):
    id = AutoField('primary key', primary_key=True)
    user = models.ForeignKey('UserAccount', verbose_name="user object")
    points = models.IntegerField('Age', null=True, blank=True)

    objects = MongoDBManager()

    class Meta:
        db_table = 'points'


class Behaviour(models.Model):
    id = AutoField('primary key', primary_key=True)
    behaviour_name = models.CharField('Class', max_length=500, blank=True)
    points = models.IntegerField('Age', null=True, blank=True)
    
    objects = MongoDBManager()

    class Meta:
        db_table = 'behaviour'

    
