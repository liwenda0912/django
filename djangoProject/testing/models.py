from django.db import models

TYPE = [
    (0, 'app'),
    (1, 'web')
]


# Create your models here.

class Name(models.Model):
    test = models.CharField(max_length=200, blank=False, verbose_name='测试名称')
    ttype = models.SmallIntegerField(blank=False, choices=TYPE, verbose_name="测试类型")
    subject = models.CharField(max_length=200, blank=False, verbose_name="测试对象")

    class Meta:
        verbose_name = '测试项目管理'
        verbose_name_plural = verbose_name


class Name1(models.Model):
    test = models.CharField(max_length=200, blank=False, verbose_name='测试名称')
    ttype = models.SmallIntegerField(blank=False, choices=TYPE, verbose_name="测试类型")
    subject = models.CharField(max_length=200, blank=False, verbose_name="测试对象")

    class Meta:
        verbose_name = '数据项目管理'
        verbose_name_plural = verbose_name


class Name2(models.Model):
    subject = models.CharField(max_length=200, blank=False, verbose_name="测试对象")
    name = models.ForeignKey(Name, on_delete=models.CASCADE, )


# Register your models here

class Taobao(models.Model):
    name = models.CharField(max_length=20, blank=False, verbose_name='名称')
    price = models.FloatField(max_length=10, blank=False, verbose_name='价格')
    num = models.IntegerField(blank=False, verbose_name='月售')

    class Meta:
        verbose_name = 'taobao数据项目管理'
        verbose_name_plural = verbose_name



