# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
<<<<<<< HEAD
from .models import Shop


# def index(request):
#     return render(request, "test1.html", {
#         'shop_list': Shop.objects.all(),
#     })
=======
from .models import AppBook
from django.views import generic

def AppBook(request):
    app_book = AppBook.objects.all()
    return render(request, "test1.html"), {"app_book": app_book}

# class AppBook(generic.TemplateView):
#     def get(self, request, *args, **kwargs):
#         template_name = 'test1.html'
#         app_book = AppBook.objects.all()
#         return render(request, template_name), {"app_book": app_book}
>>>>>>> d26c6b252f956a34c03b4352e42b3882814a37b0

def index(request):
    return render(request, "charts.html")

# def index(request):
#     shop_list = Shop.objects.all()
#     context = {'shop_list':shop_list}
#     return render(request, "test1.html", context)


def shop_test(request):
    shop_list = Shop.objects.all()
    context = {"shop_list": shop_list}
    return render(request, "charts.html", context)



#@login_required(login_url="/login/") = 로그인 시스템 있으면 필요
# 첫번째 페이지 지정
# def index(request):
#     return render(request, "charts.html")

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
