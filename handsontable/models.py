# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Header(models.Model):
    update_at = models.DateTimeField('UpdateAt')

class Detail(models.Model):
    header = models.ForeignKey(Header)
    product_name = models.CharField('Product_Name', max_length=255)
    purchase_date = models.DateTimeField('Date')
    customer_name = models.CharField('Customer_Name', max_length=255)
    price = models.DecimalField('Price', max_digits=10, decimal_places=0)