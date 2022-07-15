import sqlite3

import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from pyecharts.charts import Bar
from pyecharts import options as opts
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Line, Grid, Page, Scatter, EffectScatter  # 动态散点图

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./testing/templates"))


# Create your views here.


# 设置请求路径
# http://127.0.0.1:8000/at/add?x=1&y=2
def add(request):
    # 获取参数
    a = request.GET.get('x')
    b = request.GET.get('y')
    return HttpResponse(int(a) + int(b))


def index(request):
    name = []
    price = []
    num = []
    conn = sqlite3.connect('db.sqlite3')  # 创建连接到test2.db
    d = conn.cursor()  # 获取游标
    sql = '''
     select name, price,num from testing_taobao
   '''
    data = d.execute(sql)
    for i in data:
        n = 0
        name.append(i[0])
        price.append(i[1])
        num.append(i[2])
        n = n + 1
        if n >= 10:
            break
    conn.commit()
    conn.close()
    t = [10, 20, 30, 40, 50, 60]
    c = (Bar()
         .add_xaxis(name)
         .add_yaxis("月售", num)
         .add_yaxis("价格", price)
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"), legend_opts=opts.LegendOpts(),
                          visualmap_opts=opts.VisualMapOpts(is_show=True), toolbox_opts=opts.ToolboxOpts(),
                          ))

    s = [20, 10, 60, 50]
    f = [1, 2, 3, 4]

    d = (Line()
         .add_xaxis(name)
         .add_yaxis("月售", num)
         .add_yaxis("价格", price)

         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"),
                          legend_opts=opts.LegendOpts(is_show=True),
                          visualmap_opts=opts.VisualMapOpts(is_show=True), toolbox_opts=opts.ToolboxOpts(),

                          )
         )
    p = (Pie()
         .add('123', [list(i) for i in zip(name[:10], num[:10])],
              radius=['30%', '50%']
              , rosetype='radius'
              )
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"), legend_opts=opts.LegendOpts(),
                          visualmap_opts=opts.VisualMapOpts(is_show=True), toolbox_opts=opts.ToolboxOpts())
         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))

         )

    r = (EffectScatter()  # 动态散点图
         .add_xaxis(['1', '2'])
         .add_yaxis('t', num, symbol_size=20)
         .add_yaxis('b', t, symbol_size=30)
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"), toolbox_opts=opts.ToolboxOpts()
                          , visualmap_opts=opts.VisualMapOpts(is_show=True), legend_opts=opts.LegendOpts(is_show=True))

         )
    '''g = Grid()
    g.add(c, opts.global_options.GridOpts(pos_top='50%'), )
    g.add(d, opts.global_options.GridOpts(pos_bottom='60%'))'''
    page = Page()
    page.add(d, c, p, r)
    return HttpResponse(page.render_embed())
