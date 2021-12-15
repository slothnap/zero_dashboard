# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

# path(route, view, kwargs, name)
# route = URL 패턴을 가진 문자열
# view = 장고에서 일치하는 패턴을 찾으면, HttpRequest 객체를 첫번째 인수로 하고,
#        경로로 부터 캡처된 값을 키워드 인수로하여 특정한 view 함수를 호출합니다.
# kwargs = 임의의 키워드 인수들은 목표한 view에사전형으로 전달됩니다.
# name = URL에 이름을 지으면, 템플릿을 포함한 Django 어디에서나 명확하게 참조할 수 있습니다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app.urls")),            # 기능
    path("", include("authentication.urls"))  # 계정

]
