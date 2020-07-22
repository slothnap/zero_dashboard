# -*- encoding: utf-8 -*-
# python manage.py makemigrations
# python manage.py migrate
# python manage.py inspectdb
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    name = models.CharField(max_length=100)
    day1 = models.IntegerField(default=0)
    day2 = models.IntegerField(default=0)
    day3 = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class AppDashboard(models.Model):
    dvsn = models.CharField(primary_key=True, max_length=50)
    no   = models.IntegerField(blank=True, null=True)
    day1 = models.IntegerField(blank=True, null=True)
    day2 = models.IntegerField(blank=True, null=True)
    day3 = models.IntegerField(blank=True, null=True)
    day4 = models.IntegerField(blank=True, null=True)
    day5 = models.IntegerField(blank=True, null=True)
    day6 = models.IntegerField(blank=True, null=True)
    day7 = models.IntegerField(blank=True, null=True)
    day8 = models.IntegerField(blank=True, null=True)
    day9 = models.IntegerField(blank=True, null=True)
    day10 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.dvsn

