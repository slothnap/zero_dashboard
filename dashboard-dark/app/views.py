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
from .models import Dazero
import app.sql_list.sql_list
from django.views import generic
from django.db import connection

##############################################################################
################################## 핵심 ######################################
##############################################################################
# SQL 데이터 가져오기
# 명령어: winlotto
def WinLottoView(request):

    winlottos = []
    winlottos = app.sql_list.sql_list.GetWin()

    return render(request, 'dashboard_list/win_number.html', {"winlottos": winlottos})
    
################################################################################################################
################################################################################################################
################################################################################################################
# 패턴별 sql 가져오기
# 명령어: ptnlotto
def PtnLottoView(request):
    
    ### 값 받기 처리 ###
    g_seq  = request.GET.get('seq')
    g_pt30 = request.GET.get('pt30')
    g_pt10 = request.GET.get('pt10')
    g_pt5  = request.GET.get('pt5')
    g_pt3  = request.GET.get('pt3')  

    ### 최초 값 처리 ###
    if g_seq != None: 
        seq,pt3,pt5,pt10,pt30 = 1007,g_pt3,g_pt5,g_pt10,g_pt30 
    else:
        seq,pt3,pt5,pt10,pt30 = 1007,0,1,5,0


    ### 최초 넣고 ###
    ptnlottos = []
    ptnlottos = app.sql_list.sql_list.GetNumber(seq,pt3,pt5,pt10,pt30)

    ### 필요한 만큼 더 넣고 ###
    for i in range(0, 4):
        ptnlottos = ptnlottos + app.sql_list.sql_list.GetNumber(seq,pt3,pt5,pt10,pt30)

    return render(request, 'dashboard_list/ptn_number.html', {"ptnlottos": ptnlottos})



##############################################################################
################################## 샘플 ######################################
##############################################################################
# 매출값 가져오기
# def sales_simsale(request):
#     # 테이블 값 가져오기
#     sales_result = DaDashboardSimsale.objects.values()
#     # 쿼리셋 => list로
#     sales_list = [entry for entry in sales_result]
#     context = {"sales_list": sales_list}
#     return render(request, "sales/sales_simsale.html", context)


##############################################################################
############################### 기본 설정 #####################################
##############################################################################
#@login_required(login_url="/login/") = 로그인 시스템 있으면 필요
# 첫번째 페이지 지정
def index(request):
    return render(request, "example/index.html")


# @login_required(login_url="/login/") = 로그인 시스템 있으면 필요
# 모든 html 파일 열게
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        # load_template = request.path.split('/')[-1]
        
        # 처음 "/"만 없애기
        load_template = request.path[1:] 
        print(load_template)
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:
        html_template = loader.get_template( 'example/error/error-404.html' )
        return HttpResponse(html_template.render(context, request))
        
    except:
        html_template = loader.get_template( 'example/error/error-500.html' )
        return HttpResponse(html_template.render(context, request))

##############################################################################
##############################################################################
##############################################################################



