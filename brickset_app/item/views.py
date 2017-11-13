from django.shortcuts import render

# Create your views here.

# HttpResponseクラスのインポート
# from django.http import HttpResponse
from django.template.response import TemplateResponse

# hello()関数
def hello(request):

    # return HttpResponse('Hello World!')

    # テンプレートに渡す辞書
    context = {'message':'メッセージ'}
    return TemplateResponse(request, 'item/message.html', context=context)
