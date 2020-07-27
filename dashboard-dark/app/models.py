# -*- encoding: utf-8 -*-
# python manage.py makemigrations
# python manage.py migrate
# python manage.py inspectdb
# python manage.py runserver 192.168.102.130:8000
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

class Dashboard(models.Model):
    no = models.IntegerField(primary_key=True)
    app = models.CharField(max_length=12)
    cntn = models.CharField(max_length=50)
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
        return self.no

