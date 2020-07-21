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

