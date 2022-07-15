from django.contrib import admin

from testing.models import Name, Name2, Name1, Taobao
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


class TaobaoAdmin(admin.ModelAdmin):
    list_display_links = ('name', 'price', 'num')
    list_display = ('name', 'price', 'num')
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Taobao, TaobaoAdmin)


class Name1Admin(admin.ModelAdmin):
    list_display_links = ('test', 'subject', 'ttype')
    list_display = ('test', 'subject', 'ttype')
    search_fields = ('test',)
    fieldsets = (['test', {'fields': ('test', 'subject', 'ttype')}],)
    list_filter = ('test',)


admin.site.register(Name1, Name1Admin)


class TagInline(admin.TabularInline):
    model = Name2


class NameAdmin(admin.ModelAdmin):
    list_display_links = ('test', 'subject', 'ttype')
    list_display = ('test', 'subject', 'ttype')
    inlines = [TagInline]
    search_fields = ('test',)
    fieldsets = (['test', {'fields': ('test', 'subject', 'ttype')}],)
    list_filter = ('test',)


# 导航栏优化

admin.site.register(Name, NameAdmin)  # 注册页面格式

# 全局优化

admin.site.site_header = '平台管理'
admin.site.site_title = '后台'
