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

    ### 당첨 번호 ###
    winlottos = []
    winlottos = app.sql_list.sql_list.GetWin()

    ### 최신 번호 ###
    lastwins = []
    lastwins = app.sql_list.sql_list.GetLastWin()

    ### 최신 번호 ###
    numallcnts = []
    numallcnts = app.sql_list.sql_list.GetNumAllCnt()

    ### 당첨 패턴 ###
    getwinpattens = []
    getwinpattens = app.sql_list.sql_list.GetWinPatten()

    context = {
                "winlottos": winlottos
              , "lastwins": lastwins
              , "getwinpattens": getwinpattens
              , "numallcnts": numallcnts
              }
    return render(request, 'dashboard_list/win_number.html', context)
    
################################################################################################################
################################################################################################################
################################################################################################################
# 패턴별 sql 가져오기
# 명령어: ptnlotto
def PtnLottoView(request):
    
    ### 값 받기 처리 ###
    g_seq  = request.GET.get('seq')
    g_pt3  = request.GET.get('pt3')
    g_pt5  = request.GET.get('pt5')
    g_pt10 = request.GET.get('pt10')
    g_pt30 = request.GET.get('pt30')

    if g_seq != None: 
        pt3,pt5,pt10,pt30 = g_pt3,g_pt5,g_pt10,g_pt30 
    else:
        pt3,pt5,pt10,pt30 = 0,5,0,1


    ### 최초 넣고 ###
    ptnlottos = []
    ptnlottos = app.sql_list.sql_list.GetNumber(pt3,pt5,pt10,pt30)

    for i in range(0, 4):
        ptnlottos = ptnlottos + app.sql_list.sql_list.GetNumber(pt3,pt5,pt10,pt30)


    ### 패턴 다음 경우의 수 ###
    p1,p2,p3,p4 = 3,1,1,1 

    nextpattens = []
    nextpattens = app.sql_list.sql_list.Next_patten(p1,p2,p3,p4)


    ### 보내기 ###
    context = {
                "ptnlottos": ptnlottos
              , "nextpattens": nextpattens
              }
    return render(request, 'dashboard_list/ptn_number.html', context)

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



