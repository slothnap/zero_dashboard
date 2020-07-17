# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AppBook(models.Model):
    isbn = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'app_book'

