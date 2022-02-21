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

# MODEL 데이터값 가져오기
def zero_view(request):
    zeros = Dazero.objects.all() # Dazero 테이블의 모든 객체 불어와서 zeros 변수에 저장
    print(type(zeros))
    return render(request, 'sales/index2.html', {"zeros": zeros})


# SQL 데이터 가져오기
# 명령어: bookstore
def BookListView(request):

    try:
        cursor = connection.cursor()
        
        sql = """
              select seq, n1, n2, n3, n4, n5, n6
                from innodb.lotto
               where seq = (select max(seq) from innodb.lotto)
              """
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
        
    except:
        connection.rollback()
        print("Failed selecting in BookListView")

    return render(request, 'sales/lotto_number_cnt.html', {"lottos": lottos})
    #return render(request, 'sales/index3.html', {"lottos": lottos})
    


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
#     #return render(request, "sales/sales_simsale.html", context)
#     return render(request, "sales/sales_simsale.html")


##############################################################################
############################### 기본 설정 #####################################
##############################################################################

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
