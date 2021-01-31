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
from .models import DaDashboardSimsale
from django.views import generic

# 매출값 가져오기

def sales_simsale(request):
    # 테이블 값 가져오기
    #sales_result = DaDashboardSimsale.objects.values()

    # 쿼리셋 => list로
    #sales_list = [entry for entry in sales_result]
    #context = {"sales_list": sales_list}
    #return render(request, "sales/sales_simsale.html", context)

    return render(request, "sales/sales_simsale.html")


def lotto_cnt(request):
#     list_result2 = DaDashboardSimsale.objects.values()
#
#     # 쿼리셋 => list로
#     dashboard_list = [entry for entry in list_result2]
#     context = {"dashboard_list": dashboard_list}
#     return render(request, "sales/sales_sale09.html", context)

    return render(request, "sales/lotto_number_cnt.html")


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
