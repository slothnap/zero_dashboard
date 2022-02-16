# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models


class Dazero(models.Model):
    id        = models.IntegerField(primary_key=True, null=False)
    title     = models.CharField(max_length=100)
    update_dt = models.DateTimeField(auto_now=True)

    class Meta:
        # 테이블 이름
        db_table = 'da_zero' 



