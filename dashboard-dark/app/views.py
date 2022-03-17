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
from django.views import generic
from django.db import connection

##############################################################################
################################## 핵심 ######################################
##############################################################################

# SQL 데이터 가져오기
# 명령어: winlotto
def WinLottoView(request):

    try:
        cursor = connection.cursor()

        sql = """
                select seq, n1, n2, n3, n4, n5, n6
                from innodb.lotto
               where 1=1
                 and seq between 1000 and (select max(seq) from innodb.lotto)
               order by 1 desc
               """
        #print(sql)

        result = cursor.execute(sql)
        datas = cursor.fetchall()
    
        connection.commit()
        connection.close()

        winlottos = []
        for data in datas:
            row = {'seq': data[0],
                   'n1': data[1],
                   'n2': data[2],
                   'n3': data[3],
                   'n4': data[4],
                   'n5': data[5],
                   'n6': data[6]}
            winlottos.append(row)

    except:
        connection.rollback()
        print("Failed selecting in WinLottoView")

    return render(request, 'dashboard_list/win_number.html', {"winlottos": winlottos})
    
########################################################
def PtnLottoView(request):
    turn = request.GET.get('turn')
    
    pt30 = request.GET.get('pt30')
    pt10 = request.GET.get('pt10')
    pt5  = request.GET.get('pt5')
    pt3  = request.GET.get('pt3')  

    print(f"{pt30}, {pt10}, {pt5}, {pt3}")

    if turn != None: 
        turn2 = f"""
                and seq between 980 and {turn}
                order by 1 desc
                """    
    else:
        turn2 = """
                and seq between 1000 and (select max(seq) from innodb.lotto)
                order by 1 desc
                """
    try:
        cursor = connection.cursor()

        sql = f"""
                select seq, n1, n2, n3, n4, n5, n6
                from innodb.lotto
               where 1=1
                    {turn2}
               """
        print(sql)

        result = cursor.execute(sql)
        datas = cursor.fetchall()
    
        connection.commit()
        connection.close()

        lottos = []
        for data in datas:
            row = {'seq': data[0],
                   'n1': data[1],
                   'n2': data[2],
                   'n3': data[3],
                   'n4': data[4],
                   'n5': data[5],
                   'n6': data[6]}
            lottos.append(row)
        
        #print(type(lottos))
    except:
        connection.rollback()
        print("Failed selecting in WinLottoView")

    return render(request, 'dashboard_list/ptn_number.html', {"lottos": lottos})



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