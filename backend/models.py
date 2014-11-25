# coding: utf-8
from django.db import models

# Create your models here.
class Community(models.Model):
	name = models.CharField(verbose_name=u'名称', max_length=255)
	cover = models.URLField(verbose_name=u'截图')
	desc = models.TextField(verbose_name=u'介绍')


class Gift(models.Model):
	name = models.CharField(verbose_name=u'名称', max_length=255)
	cover = models.URLField(verbose_name=u'截图')
	desc = models.TextField(verbose_name=u'介绍')


class StoreItem(models.Model):
	community = models.ForeignKey(Community)
	gift = models.ForeignKey(Gift)


class Order(models.Model):
	community = models.ForeignKey(Community)
	username = models.CharField(verbose_name=u'用户名', max_length=32)
	mobile = models.CharField(verbose_name=u'手机号',max_length=11)
	date = models.DateTimeField(verbose_name=u'时间',auto_now_add=True, blank=True)
	count = models.IntegerField(verbose_name=u'小计')


class OrderItem(models.Model):
	order = models.ForeignKey(Order)
	gift = models.ForeignKey(Gift)
	number = models.IntegerField(verbose_name=u'数量')