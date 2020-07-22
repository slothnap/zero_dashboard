# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
from .models import Shop, AppDashboard
from django.views import generic

# DB값 가져오기
def shop_test(request):
    list_result = Shop.objects.values()

    # 쿼리셋 => list로
    shop_list = [entry for entry in list_result]
    context = {"shop_list": shop_list}
    return render(request, "charts.html", context)


def dashboard_app(request):
    list_result2 = AppDashboard.objects.values()

    # 쿼리셋 => list로
    dashboard_list = [entry for entry in list_result2]
    context = {"dashboard_list": dashboard_list}
    return render(request, "test2.html", context)


#@login_required(login_url="/login/") = 로그인 시스템 있으면 필요
# 첫번째 페이지 지정
def index(request):
    return render(request, "index.html")

# @login_required(login_url="/login/") = 로그인 시스템 있으면 필요
# 모든 html 파일 열게
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
