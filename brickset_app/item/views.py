from django.shortcuts import render

# Create your views here.

# HttpResponseクラスのインポート
# from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.http import HttpResponse

import datetime

# hello()関数
def hello(request):

    # return HttpResponse('Hello World!')

    # テンプレートに渡す辞書
    # context = {'message':'メッセージ'}
    # return TemplateResponse(request, 'item/message.html', context=context)

    context = {
        'headers':{
            'scheme':request.scheme,
            'path':request.path,
            'method':request.method,
            'content_length':request.META['CONTENT_LENGTH'],
            'http_accept':request.META['HTTP_ACCEPT_LANGUAGE'],
            'user_agent':request.META['HTTP_USER_AGENT'],
            'remote_addr':request.META['REMOTE_ADDR'],
        }
    }
    return TemplateResponse(request, 'item/header.html', context)

    # テンプレートに渡す辞書
    # context = {'today':datetime.date.today()}
    # return TemplateResponse(request, 'item/message.html', context=context)


def post(request, post_id):
    return HttpResponse('post_idは = {}です'.format(post_id))

def news(request, slug):
    return HttpResponse('slugは = {}です'.format(slug))
