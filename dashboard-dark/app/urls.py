# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views



urlpatterns = [
    # Matches any html file
    # 모든 html 파일 연동되게
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    # 첫번째 페이지 나오게
    path('', views.index, name='index'),
]
