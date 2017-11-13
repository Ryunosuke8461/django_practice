from django.contrib import admin

# Register your models here.

# Item, WishListモデルをインポート
from .models import Item, WishList

# 管理サイトへのモデルの登録
admin.site.register(Item)
admin.site.register(WishList)
