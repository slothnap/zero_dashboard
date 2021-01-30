# -*- encoding: utf-8 -*-
# python manage.py makemigrations
# python manage.py migrate
# python manage.py inspectdb
# python manage.py runserver 192.168.102.130:8000
# python manage.py runserver 192.168.35.133:8000
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

class DaDashboardSimsale(models.Model):
    sno = models.IntegerField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 'da_dashboard_simsale'
        unique_together = (('sno', 'cntn'),)



