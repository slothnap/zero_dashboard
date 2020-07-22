# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Shop, AppDashboard

# Register your models here.
admin.site.register(Shop)
admin.site.register(AppDashboard)

